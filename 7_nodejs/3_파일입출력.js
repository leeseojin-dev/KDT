/*
    파일 입출력⭐
    - fs(file system) 모듈을 사용해서 파일을 읽고 쓰는 작업을 수행
    - (백엔드에서 파일을 읽고 쓰는 것이 중요.
        end() 안에 html을 직접 작성하지 않고 파일로 보내는 경우.
        모든 내용을 db에 저장하면, 비용 발생. 잘 열어보지 않는 파일은 txt로 저장하는 것도 방법) 
*/

const fs = require("fs")

// 1. 동기 방식으로 파일 읽기
const data = fs.readFileSync("./example1.txt", "utf8")         // sync : 동기
console.log("파일 내용: ", data)

// 2. 비동기 방식으로 파일 읽기
// error 객체가 앞
// 동기와 비동기 형식이 다르니 잘 알아두기
fs.readFile("example2.txt", "utf8", (err, data) => {         // 콜백으로 익명 함수 작성
    if(err) {
        console.log("파일 읽기 실패: ", err)
        return
    }
    console.log("파일 내용: ", data)
})

/*
    *현재 없는 example.txt를 읽어오면? 에러 난 것이 아니고 에러 처리를 한 것임!
    
    비동기 방식은 에러 처리가 기본적으로 있음
    -> 동기 방식의 메서드는 에러처리가 없고, 비동기 방식의 메서드는 에러처리가 있음
    -> 동기 방식의 메서드에서는 에러처리를 위해 무조건 try-catch문을 사용
    *동기 비동기의 좋고 나쁨은 없음. 무조건 처리해야하는 코드들은 동기로 처리, 나중에 처리해도 되는 것은 비동기로 처리
*/
fs.readFile("example.txt", "utf8", (err, data) => {         // 콜백으로 익명 함수 작성
    if(err) {
        console.log("파일 읽기 실패: ", err)
        return
    }
    console.log("파일 내용: ", data)
})

// 3. 동기 방식으로 파일 쓰기
fs.writeFileSync("output1.txt", "이 내용이 파일에 저장됩니다. 동기방식!")
console.log("파일 저장 완료 (동기)")

// 3까지 작성 후 실행해보면 2보다 3이 더 먼저 출력
// 비동기로 처리한 내용은 큐에서 꺼내서 실행은 시작하지만 끝나는 건 나중에 끝날 수 있다

// 4. 비동기 방식으로 파일 쓰기
// 읽어올 건 없으니 에러 발생 시 err 객체만 생성
fs.writeFile("output2.txt", "비동기 방식으로 저장합니다.", (err) => {
    if (err) {
        console.log("저장 실패: ", err)
        return
    }
    console.log("파일 저장 완료 (비동기)")
})

// 5. 비동기 방식으로 파일에 내용 추가
fs.appendFile("output2.txt", "\n새로운 줄이 추가됩니다.", (err) => {
    if(err) throw err           // throw err : 에러를 일부러 발생 시키는 코드
    console.log("내용 추가 완료")
})

// 6. 비동기 방식으로 파일 삭제하기
fs.unlink("output2.txt", (err) => {
    if (err) throw err
    console.log("파일 삭제 완료!!!")
})