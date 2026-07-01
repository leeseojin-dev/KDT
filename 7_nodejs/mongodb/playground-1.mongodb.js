// 데이터베이스 선택 및 생성
// AIdb DB 선택(없으면 만듦❗, 있으면 사용 -> 오타나면 그대로 새로 만들어지기 때문에 오타 조심)
use("AIdb")

// db : 지금 선택한 DB (=AIdb)
// students : 컬렉션(묶어주는 역할) (컬렉션이 없으면 생성하면서 삽입)
// insertOne() : 문서(객체)를 1개 넣는 메서드
// 데이터는 객체 형태로 작성
use("AIdb")
db.students.insertOne({
    userid: "apple",
    name: "김사과",
    age: 20,
    major: "AI",
    score: 88
})


// 여러 개 삽입 시 "배열" 사용
// insertMany() : 문서를 여러 개 넣는 메서드
use("AIdb")
db.students.insertMany([
    { name: "김사과", age: 20, major: "AI", score: 88},
    { name: "반하나", age: 25, major: "Backend", score: 91},
    { name: "오렌지", age: 30, major: "Frontend", score: 77}
])

// 전체 조회
// find() : 문서를 조회하는 기본 메서드
// {} : 조건이 없다는 뜻 (= SELECT * FROM 테이블명 과 같은 역할)
use("AIdb")
db.students.find({})

/*
    ObjectId
    - 각 문서의 12바이트(24자리 16진수) 고유한 ID로 사용되는 데이터 타입
    - SQL의 기본키와 비슷한 역할을 함
    - 각 문서의 _id 필드를 기본적으로 생성하며, 특벌히 지정하지 않으면 자동으로 ObjectId 형태로 생성
*/

/*
    $eq 같다
    $ne 같지 않다
    $gt 크다
    $gte 크거나 같다
    $lt 작다
    $lte 작거나 같다
*/
// 이름이 김사과인 학생 조회
use("AIdb")
db.students.find({ name: "김사과" })
// 점수가 80점 이상인 학생 조회
use("AIdb")
db.students.find({ score: { $gte: 80 }})
// 나이가 23살 초과인 학생 조회
use("AIdb")
db.students.find({ age: { $gt: 23 }})

// 원하는 필드만 조회 (1: 포함, 0: 제외)
// (_id는 항상 나오므로 제외시키고 싶은 경우 0지정)
use("AIdb")
db.students.find({}, { name: 1, score: 1, _id: 0 })

// 1개만 조회
db.students.find({})
db.students.findOne({ name: "김사과" })

// 점수 정렬 (1: 오름차순, -1: 내림차순)
use("AIdb")
db.students.find({}).sort({ score: 1 }) // 오름차순
use("AIdb")
db.students.find({}).sort({ score: -1 }) // 내림차순

// 개수 세기
use("AIdb")
db.students.countDocuments({})
// 특정 조건을 만족하는 학생 수
use("AIdb")
db.students.countDocuments({ score: { $gte: 80 }})

// 1개 수정
// 첫 번째 객체: 누구를 수정할지 조건 부여
// 두 번째 객체: 무엇을 어떻게 바꿀지 조건
// 김사과의 점수를 95로 수정
use("AIdb")
db.students.updateOne(
    { name: "김사과" },
    { $set: { score: 95 } }
)

// 여러 데이터 수정
use("AIdb")
db.students.updateMany(
    { major: "AI" },
    { $set: { major: "Artificial Intelligence" }}
)

// 숫자 증가시키기
// $inc: 숫자 증가시킴
use("AIdb")
db.students.updateMany(
    {}, { $inc: { score: 3 }}
)

// 1개 삭제
use("AIdb")
db.students.deleteOne({ name: "오렌지" })

// 여러 문서 삭제
// 점수가 100보다 작은 문서 모두 삭제
use("AIdb")
db.students.deleteMany({ score: { $lt: 100 }})