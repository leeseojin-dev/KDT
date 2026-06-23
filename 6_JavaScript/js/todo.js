const todoInput = document.getElementById("todoInput")
const addBtn = document.getElementById("addBtn")
const todoList = document.getElementById("todoList")
const remainingCount = document.getElementById("remainingCount")
const totalCount = document.getElementById("totalCount")

// 상태를 메모리에만 저장(새로고침하면 사라짐)
const todos = []

function render() {
    todoList.innerHTML = ""
    // [{text: "아침식사", done: false}, {text: "운동하기", done: false}, ...]
    todos.forEach((todo, index) => {        // 배열에서 꺼낸 doto와 index를 가져올 수 있음
        const li = document.createElement("li") // <li></li>
        if (todo.done) li.classList.add("done")     // classList: li 태그에 클래스 항목인 done을 만든다는 의미 <li class="done"></li>

        const left = document.createElement("div")  // <div></div>
        left.className = "left"     // <div class="left"></div>

        const checkbox = document.createElement("input")    // <input></input>
        checkbox.type = "checkbox"      // <input type="checkbox"></input>
        checkbox.checked = todo.done    // <input type="checkbox" checked="false"></input>
        checkbox.addEventListener("change", () => {     // checkbox에 change이벤트가 발생했을 때, 콜백함수 실행
            todo.done = checkbox.checked
            render()
        })

        const text = document.createElement("span")     // <span></span>
        text.className = "todo-text"        // <span class="todo-text"></span>
        text.textContent = todo.text        // <span class="todo-text">아침식사</span>

        const delBtn = document.createElement("button")
        delBtn.className = "delete-btn"
        delBtn.type = "button"
        delBtn.textContent = "삭제"
        delBtn.addEventListener("click", () => {
            todos.splice(index, 1)      // splice(): 자기 인덱스부터 1개만 지워줘
            render()
        })
        
        left.appendChild(checkbox)
        left.appendChild(text)
        left.appendChild(delBtn)

        li.appendChild(left)
        todoList.appendChild(li)
    })
    updateCounts()
}

function updateCounts() {
    
}

function addTodo() {
    const text = todoInput.value.trim()
    if(!text) return    // 입력한 글자가 없다면 리턴시켜서 종료시켜버리는 코드 필요 (가독성도 성능도 굳)

    todos.push({ text, done: false })   // todos 배열에 객체를 삽입
    // key와 value의 이름이 같으면 생략 가능 { text: text, done: false } 와 같은 말
    todoInput.value = ""        // 비워주고 포커스 주기
    todoInput.focus()
    
    render()
}

addBtn.addEventListener("click", addTodo)

todoInput.addEventListener("keydown", (e) => {      // todoInput에서 keydown이 발생했을 때, 그 이벤트 키가 Enter일 경우에 addTodo() 메서드 작동
    if(e.key === "Enter") addTodo()
})

render()        // 그냥도 실행 (무조건 한 번 실행하도록 호출)