import { useEffect, useState } from "react";
import { useParams, useNavigate, Link } from "react-router-dom";
import api from "../api/axios";
import ConfirmModal from "../components/ConfirmModal";

export default function PostDetail() {
  const { categoryId, postId } = useParams();
  const [post, setPost] = useState(null);
  const [comments, setComments] = useState([]);
  const [text, setText] = useState("");
  const [showDelete, setShowDelete] = useState(false);
  const navigate = useNavigate();

  const isLoggedIn = !!localStorage.getItem("access");

  const load = async () => {
    const [postRes, commentsRes] = await Promise.all([
      api.get(`/api/categories/${categoryId}/posts/${postId}`),
      api.get(
        `/api/categories/${categoryId}/posts/${postId}/comments`
      ),
    ]);
    setPost(postRes.data);
    setComments(commentsRes.data);
  };

  useEffect(() => {
    load();
  }, [categoryId, postId]);

  const addComment = async (e) => {
    e.preventDefault();
    if (!text.trim()) return;
    await api.post(
      `/api/categories/${categoryId}/posts/${postId}/comments`,
      {
        text,
        post: postId,
      }
    );
    setText("");
    load();
  };

  const deletePost = async () => {
    await api.delete(`/api/categories/${categoryId}/posts/${postId}`);
    navigate(`/categories/${categoryId}`);
  };

  const deleteComment = async (commentId) => {
    await api.delete(
      `/api/categories/${categoryId}/posts/${postId}/comments/${commentId}`
    );
    load();
  };

  if (!post) return <div className="page-container">Kraunasi</div>;

  return (
    <div className="page-container">
      <Link
        to={`/categories/${categoryId}`}
        className="text-decoration-none mb-2 d-inline-flex align-items-center"
      >
        <i className="fa-solid fa-chevron-left me-1"></i> Atgal prie post'u
      </Link>

      <div className="card-forum mb-3">
        <div className="d-flex justify-content-between align-items-start">
          <div>
            <h3 className="mb-2">{post.title}</h3>
            <p style={{ color: "#e5e7eb" }}>{post.text}</p>
          </div>
          <button
            className="btn btn-outline-danger btn-sm btn-pill"
            onClick={() => setShowDelete(true)}
          >
            Delete post
          </button>
        </div>
      </div>

      <h5 className="mb-3">Komentarai ({comments.length})</h5>

      {comments.map((c) => (
        <div key={c.id} className="card-forum">
          <div className="d-flex justify-content-between align-items-start">
            <p className="mb-1">{c.text}</p>
            <button
              className="btn btn-sm btn-outline-danger btn-pill"
              onClick={() => deleteComment(c.id)}
            >
              Delete
            </button>
          </div>
        </div>
      ))}

      {comments.length === 0 && (
        <p className="text-muted">Komentarų nėra</p>
      )}

      {isLoggedIn && (
        <div className="card-forum mt-3">
          <h6 className="mb-2">Pridėkite komentarą</h6>
          <form onSubmit={addComment}>
            <textarea
              className="form-control mb-2"
              rows={3}
              placeholder="Komentaras"
              value={text}
              onChange={(e) => setText(e.target.value)}
            />
            <button className="btn btn-primary btn-pill" type="submit">
              Reply
            </button>
          </form>
        </div>
      )}

      <ConfirmModal
        show={showDelete}
        title="Ištrinti postą"
        text="Ar tikrai norite ištrinti? Komentarai taip pat bus ištrinti."
        onConfirm={deletePost}
        onClose={() => setShowDelete(false)}
      />
    </div>
  );
}
