function sendit() {
    const userid = document.getElementById("userid")
    const userpw = document.getElementById("userpw")
    const userpw_re = document.getElementById("userpw_re")
    const name = document.getElementById("name")
    const phone = document.getElementById("phone")
    const email = document.getElementById("email")


    const expIdText = /^[A-Za-z0-9]{4,20}$/
    /*
        (?=.*): 어디엔가 원하는 패턴이 하나라도 있어야 함
        (?=.*[A-Za-z]): 영문자가 최소 1개 이상 있어야 함
        (?=.*\d): 숫자가 최소 1개 이상 있어야 함
        (?=,*[!@#$%^&*()]): 제시된 특수 문자가 최소 1개 이상 있어야 함
        
    */
    const expPwTest = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*()])[A-Za-z\d!@#$%^&*()]{8,20}$/
    const expNameTest = /^[가-힣]{3,4}$/
    const expPhoneTest = /^010-\d[0-9]{3,4}-\d[0-9]{4}$/
    const expEmailTest = /^[^\s@]+@[^\s@]+\.[^\s@]$/
    
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
        alert("이름을 입력하세요")
        name.focus()
        return false
    }

    if(!expPhoneTest.test(phone.value)){
        alert("휴대폰 번호를 입력하세요")
        phone.focus()
        return false
    }

    if(!expEmailTest.test(email.value)){
        alert("이메일을 입력하세요")
        email.focus()
        return false
    }
}