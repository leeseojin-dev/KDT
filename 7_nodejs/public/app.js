// 3개의 객체 가져오기
const memoInput = document.getElementById("memoInput")
const addBtn = document.getElementById("addBtn")
const memoList = document.getElementById("memoList")

// 1. 메모 불러오기
async function loadMemos() {
    try {
        // fetch(): 어느 서버에 붙일지 위치를 작성. GET으로 접속(기본값). json으로 받아옴
        const response = await fetch("/memos")       
        const data = await response.json()      // 자바스크립트의 json 타입으로 변경
        renderMemos(data.memos)
    } catch(error) {
        console.log("메모 조회 실패: ", error)
    }
}


// 3. 메모 추가하기
// 이벤트 등록
addBtn.addEventListener("click", async () => {
    // async: 다른 사람이 버튼을 누르고 또 다른 사람이 눌렀을 때 지연되지 않도록 (동시 진행되도록)
    const text = memoInput.value.trim()
    if(!text){
        alert("메모를 입력하세요")
        return 
    }

    try {
        const response = await fetch("/memo", {
            method: "POST",         
            headers: {
                "Content-Type": "application/json"      // json 타입으로 보낸다고 headers로 전달
            },
            body: JSON.stringify({ text })      // 객체를 보낼 때는 문자열로 바꿔서
        })

        // 서버에서 응답 받기 -> json으로 변환하여 data에 저장
        const data = await response.json()
        memoInput.value = ""
        renderMemos(data.memos)
    } catch(error) {
        console.log("메모 추가 실패: ", error)
    }
})




// 2. 렌더링 함수
function renderMemos(memos) {        // memos는 배열로 가져옴 (GET에서 toArray()로 보냈기 때문. 9_메모.js 확인)
    memoList.innerHTML = ""

    memos.forEach((memo) => {
        const li = document.createElement("li")     // <li></li>
        li.className = "memo-item"                  // <li class="memo-item"></li>
        li.innerHTML = `
            <span>${memo.text}</span>
            <div class="memo-buttons">
                <button onclick="editMemo('${memo._id}')">수정</button>
                <button onclick="deleteMemo('${memo._id}')">삭제</button>
            </div>
        `
        memoList.appendChild(li)
    })
}



// 4. 메모 삭제
// renderMemos에서 삭제버튼을 만들고 있기 때문에 여기에 onclick 메서드 추가
async function deleteMemo(id) {      
    const check = confirm("정말 삭제하시겠습니까?")       // confirm(): true/false로 반환
    // console.log(check)
    // console.log(id)
    if(!check) return           // false일 경우 함수 종료

    try {
        const response = await fetch(`/memos/${id}`, {
            method: "DELETE"
        })
        const data = await response.json()
        renderMemos(data.memos)     // 지워진 결과를 받아서 렌더
    } catch(error) {
        console.log("메모 삭제 실패: ", error)
    }
}



// 5. 메모 수정
// 삭제와 마찬가지로 renderMemos에서 수정버튼을 만들고 있기 때문에 여기에 onclick 메서드 추가
async function editMemo(id) {
    // prompt(): 입력받는 창. 잘 사용안하지만, 간단하게 예제로 사용해보자
    const newText = prompt("수정할 내용을 입력하세요.")      
    // console.log(newText)
    if(!newText || newText.trim() === "") return         // 내용이 없을 경우 함수 종료

    try{
        const response = await fetch(`/memos/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: newText })
        })
        // loadMemos()         // reload 해도 ㅇㅇ

        // *loadMemos() 대신 아래 코드 사용해도 동일하게 정상 작동*
        // if (response.ok){
        //     const data = await response.json()
        //     renderMemos(data.memos)  
        //     alert("메모 수정 성공")
        // }
    } catch(error) {
        console.log("메모 수정 실패: ", error)
    }
}

loadMemos()