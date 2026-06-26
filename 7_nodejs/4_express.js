/*
    Express
    - node.js 환경에서 가장 널리 사용되는 웹 애플리케이션 프레임워크로, 서버를 쉽고 빠르게 구축할 수 있도록 다양한 기능을 제공
    - 기본적인 HTTP 모듈보다 훨씬 간단하게 라우팅 처리, 요청/응답 객체 관리, 미들웨어 설정, 정적 파일 제공, 템플릿 엔진 연결 등을 할 수 있어 개발 생산성을 크게 높여줌

        npm install express

    라우팅
    - 클라이언트가 어떤 URL과 HTTP 메서드(GET, POST)로 요청을 보냈을 때 그 요청을 어떤 코드가 처리할지 연결해주는 규칙

    미들웨어
    - 요청(request)과 응답(response) 사이에서 중간에 실행되는 함수로, 클라이언트의 요청을 직접 처리하기보다는 가공/검사/추가 작업을 담당하는 역할을 함
    - 요청 로그를 남기거나, JSON 데이터를 파싱하거나 로그인 여부를 검사하거나, 에러를 처리하는 기능들이 모두 미들웨어

    정적파일
    - 서버에서 별도의 처리 없이 그대로 클라이언트에게 전달되는 파일
    - 대표적으로 HTML, CSS, Javascript, 이미지, 폰트 파일 등이 있으며, 사용자의 요청이 들어오면 서버는 내용을 가공하지 않고 저장된 그대로 응답

    EJS(Embedded JavaScript)
    - EJS는 HTML 안에 Javascript 코드를 삽입해 서버 데이터를 동적으로 렌더링할 수 있게 해주는 node.js용 템플릿 엔진
    - <%= %>, <% %> 안에서 로직을 작성하여 사용
        npm i ejs

        1. username 값을 출력
        <h1><%=username%></h1>  

        2. 조건문
        // 자바 스크립트 안에 html 코드 작성이 불가하므로 아래 처럼 작성
        <%
            if(isLogin) {
        %>
            <p>로그인 상태입니다.</p>
        <%
            }esle{
        %>
            <p>로그인이 필요합니다.</p>
        <%
            }
        %>

        3. 반복문
        <%
            const users = ['김사과', '반하나', '오렌지']
        %>
            <ul>
        <%
            for(let i=0; i<users.length; i++ {
        %>
            <li><%=users[i]%></li>
        <%
            }
        %>
            </ul>

        <ul>
        <% users.forEach(user => { %>
            <li><%=user%></li>   
        <%})%>
        </ul>

    템플릿 엔진
    - HTML과 데이터를 결합해 동적인 화면을 만들어주는 도구
    - 서버에서 전달한 값을 HTML 안에 삽입해 최종 페이지를 생성하며, 반복문/조건문 같은 로직도 템플릿 내부에서 처리할 수 있음

    
*/

// express 모듈을 불러와서 express객체를 생성. 포트번호 3000번으로 미리 저장
const express = require("express")      // python의 import문이라고 생각
const path = require("path")
const app = express()
const port = 3000

// use() : 미들웨어 등록
// express.static() 메서드 : public이라는 폴더
// app.use(express.static('public')) // root에서 접근
app.use("/static", express.static('public'))    // http://127.0.0.1:3000/static/spring.png 에서 접근
app.use(express.urlencoded({ extended: true }))   // post 데이터를 받아오기 위한 코드

// EJS 설정
app.set("view engine", "ejs")
app.set("views", path.join(__dirname, "view"))  // __dirname: 현재 디렉터리


app.get("/", (req, res) => {
    res.send("Hello Express!")
})

// 경로와 파일명은 다를 수 있겠쥬?
// hello.ejs 파일의 name 변수로 "김사과"를 전달
app.get("/hello", (req, res) => {       // 여기의 hello는 경로 이름
    res.render("hello", { name: "김사과" })     // 여기의 hello는 확장명을 뺀 ejs 파일명
})

// get으로 submit.ejs를 호출
// submit.ejs에서 method가 post인 form태그를 만들어서 버튼을 누르면 아래의 app.post로 이동
app.get("/submit", (req, res) => {
    res.render("submit")
})

// http://127.0.0.1:3000/submit 로 실행하면 Cannot GET이라고 뜸!!
app.post("/submit", (req, res) => {
    const { name, age } = req.body      // req.body로 받아온 name과 age를 분해해서 전달
    console.log("name:", name)
    console.log("age:", age)
    res.send("post로 호출!")
    
})


app.listen(port, () => {
    console.log("서버 실행 중...")
})
