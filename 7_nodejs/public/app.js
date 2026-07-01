// 3개의 객체 가져오기
const memoInput = document.getElementById("memoInput")
const addBtn = document.getElementById("addBtn")
const memoList = document.getElementById("memoList")

// 1. 메모 불러오기
async function loadMemos() {
    try {
        const response = await fetch("/memos")        // 어느 서버에 붙일지 위치를 작성. GET으로 접속. json으로 받아옴
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
            method: "POST",         // fetch는 기본값으로 GET
            headers: {
                "Content-Type": "application/json"
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
                <button>수정</button> <button>삭제</button>
            </div>
        `
        memoList.appendChild(li)
    })
}
loadMemos()