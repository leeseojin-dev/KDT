const express = require("express")
const path = require("path")
const { MongoClient, ObjectId, ReturnDocument } = require("mongodb")

const app = express()
const PORT = 3000

// 미들웨어 등록
app.use(express.json())
app.use(express.static(path.join(__dirname, "public")))

const url = "mongodb+srv://dltjwls5669:uxw74fHcxlucgHdk@cluster0.ibgmpwa.mongodb.net/"
const client = new MongoClient(url)

const dbName = "memo"
let memoCollection

// 1. DB 연결
async function startServer() {
    try {
        await client.connect()
        console.log("MongoDB 연결 성공!!")

        const db = client.db(dbName)                // db로 바로 접근 가능
        memoCollection = db.collection("memos")     // collection(): 컬렉션까지 접근 가능한 객체

        app.listen(PORT, () => {
            console.log("서버 실행 중 ...")
        })

    } catch(error) {
        console.log("MongoDB 연결 실패: ", error)
    }
}
startServer()

// 4. GET으로 메모 검색
app.get("/memos", async(req, res) => {
    try {
        const { keyword } = req.query
        let filter = {}

        if(keyword && keyword.trim() !== ""){     // keyword가 존재하고 공백제거 후에도 데이터가 없지 않다면
            filter = {
                text: { $regex: keyword.trim(), $options: "i" }
            }
        }

        const memos = await memoCollection.find(filter).sort({ createdAt: -1 }).toArray()
        res.json({
            success: true,
            count: memos.length,
            memos
        })

    } catch(error) {
        console.log("메모 조회 오류: ", error)
        res.status(500).json({
            success: false,
            message: "메모 조회 중 오류가 발생!"
        })
    }
})


// 2. POST로 메모 추가
// 비동기로 처리한 이유: 한 사용자가 처리되는 동안 다른 사용자들도 들어오도록 하기 위해 (병목현상해결)
app.post("/memo", async(req, res) => {      
    try {
        // { text: "메모값" }
        const { text } = req.body
        if(!text || text.trim() === "") {       // text가 비어있거나, 공백제거후에도 비어있다면
            return res.status(400).json({
                success: false,
                message: "메모 내용을 입력해주세요"
            })
        }

        const newMemo = {       // 새로운 메모 객체 생성
            text: text.trim(),
            createdAt: new Date()
        }

        // 3. DB에 메모 추가
        await memoCollection.insertOne(newMemo)

        // sort({ createdAt: -1 }): 최신 순으로 정렬
        // toArray(): 가져온 데이터를 배열로 바꾸기
        const memos = await memoCollection.find().sort({ createdAt: -1 }).toArray()

        res.status(201).json({
            success: true,
            message: "메모가 추가되었습니다.",
            memos
        })

    } catch(error) {
        console.log("메모 저장 오류: ", error)
        res.status(500).json({
            success: false,
            message: "서버 오류 발생!!"
        })
    }
})
// postman으로 { text: "첫 메모" } 전송
// browse collections > clustor0 > memo > memos에 새로운 메모 추가된 것 확인 가능 


// 5. PUT으로 메모 수정
app.put("/memos/:id", async(req, res) => {
    try{
        const { id } = req.params
        const { text } = req.body

        // id가 MongoDB ObjectId 형식인지 검사하고 아니면 400에러 반환
        if(!ObjectId.isValid(id)) {
            return res.status(400).json({
                success: false,
                message: "올바르지 않은 메모 id 형식!!"
            })
        }

        if(!text || text.trim() === "") {       // text가 비어있거나, 공백제거후에도 비어있다면
            return res.status(400).json({
                success: false,
                message: "변경할 메모 내용을 입력해주세요"
            })
        }

        // findOneAndUpdate(): 하나를 찾아서 수정
        const result = await memoCollection.findOneAndUpdate(
            { _id: new ObjectId(id) },       // mongodb에서 id를 찾는다
            {
                $set: {
                    text: text.trim(),       // text를 수정한다
                    updatedAt: new Date()    // 업데이트 날짜를 추가한다
                }
            },
            {
                returnDocument: "after"     // after: 변경된 이후 값을 보여줌 / 기본값: 이전값을 보여줌. 
            }
        )

        if(!result) {       // 변경된 것이 없다면
            return res.status(404).json({
                success: false,
                message: "해당 id의 메모를 찾을 수 없습니다"
            })
        }

        res.json({
            success: true,
            message: "메모가 수정되었습니다. (PUT)",
            memo: result
        })

    } catch(error) {
        console.log("메모 수정 오류 (PUT): ", error)
        return res.status(500).json({
            success: false,
            message: "메모 수정 중 오류가 발생!!"
        })
    }
})

// 6. DELETE 메모 삭제
app.delete("/memos/:id", async(req, res) => {
    try {
        // 6-1. id 형식 검사
        const { id } = req.params

        if(!ObjectId.isValid(id)){
            return res.status(400).json({
                success: false,
                message: "올바르지 않은 메모 id 형식!!"
            })
        }

        // 6-2. 삭제 실행
        const result = await memoCollection.deleteOne(
            { _id: new ObjectId(id) }
        )
        
        if (result.deletedCount === 0) {
            return res.status(404).json({
                success: false,
                message: "삭제할 메모를 찾을 수 없습니다."
            })
        }

        // 6-3. 삭제 후 전체 목록 다시 조회
        const memos = await memoCollection.find().sort({ createdAt: -1 }).toArray()
        res.json({
            success: true,
            message: "메모가 삭제되었습니다",
            memo: result,
            count: memos.length,
            memos
        })

    } catch(error) {
        console.log("메모 삭제 오류: ", error)
        res.status(500).json({
            success: false,
            message: "메모 삭제 중 오류가 발생!!"
        })
    }
})