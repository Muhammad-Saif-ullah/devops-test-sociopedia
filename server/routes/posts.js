import express from "express";
import { getFeedPosts, getUserPosts, likePost, commentPost, deletePost } from "../controllers/posts.js";
import { verifyToken } from "../middleware/auth.js";

const router = express.Router();

/* READ */
router.get("/", verifyToken, getFeedPosts);
router.get("/:userId/posts", verifyToken, getUserPosts);

/* UPDATE */
router.patch("/:id/like", verifyToken, likePost);
router.patch("/:postId/comment", verifyToken, commentPost);

/* DELETE */
router.delete("/:postId", verifyToken, deletePost);

export default router;
