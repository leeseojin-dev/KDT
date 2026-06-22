/*
    onload : 현재 페이지가 다 로드 되었다면~ 이라는 메서드
*/
window.onload = function() {
    const ssn1 = document.getElementById("ssn1")
    ssn1.addEventListener("keyup", () => {
        if(ssn1.value.length >= 6) {
            document.getElementById("ssn2").focus()
        }
    })

    const ssn = document.querySelectorAll(".ssn")
    ssn.forEach((s) => {
        // console.log(s)
        s.addEventListener("input", () => {
            document.getElementById("ssncheck").value = "n"
        })
    })
}


function sendit() {
    const userid = document.getElementById("userid")
    const userpw = document.getElementById("userpw")
    const userpw_re = document.getElementById("userpw_re")
    const name = document.getElementById("name")
    const hp = document.getElementById("hp")
    const email = document.getElementById("email")
    const ssncheck = document.getElementById("ssncheck")
    
    const expIdText = /^[A-Za-z0-9]{4,20}$/
    /*
        (?=.*): 어디엔가 원하는 패턴이 하나라도 있어야 함
        (?=.*[A-Za-z]): 영문자가 최소 1개 이상 있어야 함
        (?=.*\d): 숫자가 최소 1개 이상 있어야 함
        (?=,*[!@#$%^&*()]): 제시된 특수 문자가 최소 1개 이상 있어야 함
        
    */
    const expPwTest = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*()])[A-Za-z\d!@#$%^&*()]{8,20}$/
    const expNameTest = /^[가-힣]+$/
    const expHpTest = /^\d{3}-\d{3,4}-\d{4}$/
    const expEmailTest = /^[A-Za-z0-9\-\.]+@[A-Za-z0-9\-]+\.[A-Za-z]+$/
    // const expEmailTest = /^[^\s@]+@[^\s@]+\.[^\s@]$/
    
    if(userid.value === ""){
        alert("아이디를 입력하세요")
        userid.focus()
        return false
    }

    if(!expIdText.test(userid.value)){
        alert("아이디는 4자 이상 20자 이하의 영문자 또는 숫자로 입력하세요")
        userid.focus()
        return false
    }

    if(!expPwTest.test(userpw.value)){
        alert("비밀번호는 8자 이상 20자 이하의 영문자, 숫자, 특수문자를 한 자 이상 꼭 포함해야 합니다")
        userpw.focus()
        return false
    }

    if(userpw.value != userpw_re.value){
        alert("비밀번호와 비밀번호 확인이 일치하지 않습니다")
        userpw_re.focus()
        return false
    }

    if(!expNameTest.test(name.value)){
        alert("이름은 한글로 입력하세요")
        name.focus()
        return false
    }

    if(!expHpTest.test(hp.value)){
        alert("휴대폰번호 형식이 일치하지 않습니다\n하이픈을 꼭 입력하세요")
        hp.focus()
        return false
    }

    if(!expEmailTest.test(email.value)){
        alert("이메일 형식이 일치하지 않습니다")
        email.focus()
        return false
    }

    if(ssncheck.value == "n") {
        alert("주민등록번호 검증을 눌러주세요")
        return false
    }

}

function checkSsn(){
    let ssncheck = document.getElementById("ssncheck")
    const ssn1 = document.getElementById("ssn1")
    const ssn2 = document.getElementById("ssn2")
    const ssn = ssn1.value + ssn2.value
    // const ssn = (ssn1.value + ssn2.value).split("").map((e) => Number(e))
    const checkarr = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    let result = 0;

    for (let i = 0; i < checkarr.length; i++) {
        result += parseInt(ssn[i] * checkarr[i])
    }

    result = (11 - (result % 11)) % 10

    if(result == parseInt(ssn[12])) {
        alert("유효한 주민등록번호입니다!")
        ssncheck.value = "y"
        
    } else {
        alert("유효하지 않은 주민등록번호입니다!")
    }
}
/*
    1. 주민등록번호 유효성 검사
    2. 앞자리 입력 후 자동으로 뒷자리 입력 칸으로 focus주는 코드 구현
    3. ssn1, ssn2 인증 후, ssn1과 ssn2를 수정하고 인증 안하고 가입완료해도 넘어가는 문제 해결하는 코드
*/