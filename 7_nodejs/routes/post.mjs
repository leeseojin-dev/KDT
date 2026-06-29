import express from "express"

const router = express.Router()

// http://127.0.0.1:3000/posts (GET)
router.get("/", (req, res) => {
    res.status(200).send("GET: /posts 글 조회")
})

// http://127.0.0.1:3000/posts (POST)
router.post("/", (req, res) => {
    res.status(201).send("POST: /posts 글 작성")
})

// http://127.0.0.1:3000/posts (PUT)
router.put("/:id", (req, res) => {
    res.status(201).send("PUT: /posts/:id 글 수정")
})

// http://127.0.0.1:3000/posts (DELETE)
router.delete("/:id", (req, res) => {
    res.status(200).send("DELETE: /posts/:id 글 삭제")
})

export default router