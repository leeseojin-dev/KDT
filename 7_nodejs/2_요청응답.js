/*
    1. 경로 설정
    http 모듈에서 경로 설정(라우팅)은 사용자의 요청 주소를 나타내는 req.url과 요청 방식인 req.method를 확인하여 조건문으로 분기 처리하는 방식으로 이루어짐

    127.0.0.1:3000/
    127.0.0.1:3000/about

    2. GET과 POST
        GET: 서버로부터 데이터를 조회할 때 사용하는 요청 방식으로, 주로 게시글 목록 보기, 검색 결과 조회, 상세 페이지 열기처럼 데이터를 가져오는 데 사용됨. GET 요청은 필요한 값을 URL 뒤에 ? key=value 형태의 쿼리 문자열로 함께 전달하며, 브라우저 주소창에 그대로 표시
        POST: 서버에 데이터를 전송하여 새로운 데이터를 생성하거나 기존 데이터를 변경할 때 사용하는 요청 방식으로, 회원 가입, 로그인, 글 작성, 파일 업로드 등에 사용됨. POST 요청은 데이터를 URL이 아니라 요청 본문(body)에 담아 보내기 때문에 주소창에 내용이 보이지 않으며, GET보다 보안성이 조금 더 높고 전송할 수 있는 데이터 양에도 제한이 거의 없음

        127.0.0.1:3000/login
        if(req.url == '/login' & req.method === 'post') {
            res.end("로그인 처리")
        }

    3. 쿼리 문자열(Query String)
    - 쿼리 문자열은 URL 뒤에 ? 기호를 기준으로 붙는 추가 데이터 전달 방식으로, 서버에 필요한 값을 함께 보내기 위해 사용됨
    - key=value 형태로 작성하며 여러 개의 값은 & 기호로 연결함 (예: ?name=김사과&age=20)
    - 주로 GET 요청에서 사용되며 검색 조건, 페이지 번호, 필터 값 등을 전달할 때 많이 활용

    *Code Runner 설치 (실행을 편하게 해주는 extensions)
        file-preference-settings-setting.json에 아래 코드 추가 
        -> ctrl + alt + n 단축키로 실행

    *nodemon
    - node.js 개발 시 자주 사용하는 유틸리티로, 소스 코드가 변경될 때마다 자동으로 서버를 재시작해주는 도구 (큰 프로젝트에서는 편할 수 있으나 개발 작은 예제에서는 별로일 수도)
        npm install -g nodemon (g: 모든 프로젝트에서 사용 가능한 글로벌 모드, 권장 x, package.json에 기록이 안돼서..)
        npm install --save-dev nodemon (해당 프로젝트에서만 사용)
    - package.json의 Scripts에 "dev": "nodemon 2_요청응답.js" 추가

    JSON
    - 자바스크립트 객체 표기법을 기반으로 한 데이터 교환 형식
    - 일반적으로 서버와 클라이언트 간에 데이터를 주고 받을 때 사용
    - 구조는 키-값 쌍으로 이루어진 객체 형태나 배열 형태를 사용

        const user = { name: "김사과", age: 20 }
        const jsonStr = JSON.stringify(user)        // 객체를 문자열로 변환
        // 네트워크를 통해 보내기 때문에 객체를 알아 들을 수 없기 때문에 문자열로 변환하여 보내야 함

        const jsonStr = "{ name: "김사과", age: 20 }"
        const userObj = JSON.parse(jsonStr)     // 문자열을 객체로 변환
    
*/
const http = require("http")
const url = require("url")      // 쿼리 스트링의 ? 뒤에 있는 문자열을 가져올 수 있는 

const server = http.createServer((req, res) => {
    // url.parse(req.url, true): true는 query string을 객체로 자동 변환
    
    if(req.url === '/') {                   // 도메인의 루트 주소를 찾는 것 (127.0.0.1:3000/)
        res.writeHead(200, {"Content-type": "text/html"})
        res.end("<h2>Hello Node.js</h2>")   // end 안의 내용 출력
    } else if(req.url === '/about') {       // (127.0.0.1:3000/about)
        res.writeHead(200, {"Content-type": "text/html"})       
        res.end("<h2>about page</h2>")
    } else if(req.url === '/api/user') {    // (127.0.0.1:3000/api/user)
        const user = {
            userid: "apple",
            name: "김사과", 
            age: 20,
            job: "AI개발자"
        }
        res.writeHead(200, {"Content-type": "application/json"})  // 받을 파일은 json 형식이야
        res.end(JSON.stringify(user))       // json형식의 문자열을 보냄
    } else {
        res.writeHead(404, {"Content-type": "text/html"})       // 이외
        res.end("<h2>error🤢</h2>")
    }
})

server.listen(3000, () => {
    console.log("서버 실행 중...!!!")
})
