import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import api from "../api/axios";

export default function CategoryPosts() {
  const { categoryId } = useParams();
  const [posts, setPosts] = useState([]);
  const [title, setTitle] = useState("");
  const [text, setText] = useState("");
  const [categoryName, setCategoryName] = useState("");

  const isLoggedIn = !!localStorage.getItem("access");

  const load = async () => {
    const [postsRes, catRes] = await Promise.all([
      api.get(`/api/categories/${categoryId}/posts`),
      api.get(`/api/categories/${categoryId}`),
    ]);
    setPosts(postsRes.data);
    setCategoryName(catRes.data.name);
  };

  useEffect(() => {
    load();
  }, [categoryId]);

  const createPost = async (e) => {
    e.preventDefault();
    if (!title.trim() || !text.trim()) return;
    await api.post(`/api/categories/${categoryId}/posts`, {
      title,
      text,
      category: categoryId,
    });
    setTitle("");
    setText("");
    load();
  };

  return (
    <div className="page-container">
      <h2 className="mb-3">Category: {categoryName}</h2>

      {isLoggedIn && (
        <div className="card-forum mb-4">
          <h5 className="mb-2">New post</h5>
          <form onSubmit={createPost}>
            <div className="mb-2">
              <input
                className="form-control"
                placeholder="Post title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
              />
            </div>
            <div className="mb-2">
              <textarea
                className="form-control"
                rows={3}
                placeholder="What do you want to share?"
                value={text}
                onChange={(e) => setText(e.target.value)}
              />
            </div>
            <button className="btn btn-primary btn-pill" type="submit">
              Publish
            </button>
          </form>
        </div>
      )}

      {posts.map((p) => (
        <Link
          key={p.id}
          to={`/categories/${categoryId}/posts/${p.id}`}
          className="card-forum"
        >
          <h5 className="mb-1">{p.title}</h5>
          <p className="mb-1" style={{ color: "#d1d5db" }}>
            {p.text.length > 120 ? p.text.slice(0, 120) + "..." : p.text}
          </p>
          <small style={{ color: "#9ca3af" }}>Open thread</small>
        </Link>
      ))}

      {posts.length === 0 && (
        <p className="text-muted">No posts in this category yet.</p>
      )}
    </div>
  );
}
