const express = require("express")
const fs = require("fs")
const path = require("path")

const app = express()
const PORT = 3000

app.set("view engine", "ejs")   // view engine을 ejs로 등록
app.set("views", path.join(__dirname, "view"))      // 어디에서 ejs 파일을 가져와야하는지 현재 폴더(__dirname)의 view라는 폴더로 경로 지정

app.use(express.urlencoded({ extended: true }))     // 폼 데이터를 읽어오기 위한 미들웨어
const filePath = path.join(__dirname, "data", "posts.txt")      // 파일 경로

// 게시물 작성
app.get("/", (req, res) => {
    res.render("write")
})
// 글을 작성 후 저장을 눌러서 posts로 보냈는데 게시물 저장의 app.post("/posts")로 들어와서 res.send("파일 저장 성공!")을 실행한 것
// 게시물 리스트인 app.get("/posts")로 들어간 것이 아님

// 게시물 저장
app.post("/posts", (req, res) => {      // 사용자는 req로 내용을 전달
    const { title, content } = req.body
    const saveText = `
    =========================
    제목: ${title}
    내용: ${content}
    작성일: ${new Date().toLocaleString()}
    =========================
    `

    fs.appendFile(filePath, saveText, "utf8", (err) => {        // appendFile() : 파일이 없으면 새로 생성 있으면 계속 추가
        if(err) {
            console.error(err)
            return res.send("파일 저장 중 오류가 발생함!")
        }
        // res.send("파일 저장 성공!")
        res.redirect("/posts")      // redirect() : get방식으로 페이지를 자동으로 이동 시키는 메서드. 게시물 리스트의 app.get("/posts")로 이동
    })     
})

// 게시물 리스트
app.get("/posts", (req, res) => {               // url 호출은 무조건 GET 사용
    fs.readFile(filePath, "utf8", (err, data) => {
        if(err) {
            console.error(err)
            return res.render("posts", { posts: "아직 저장된 게시물이 없습니다" })     // render : ejs를 서버 코드르 변환하여 처리 후 전체를 HTML로 바꿔서 사용자에게 전달
        }
        res.render("posts", { posts: data })
    })
})

app.listen(PORT, () => {
    console.log("서버 실행 중 ...")
})
