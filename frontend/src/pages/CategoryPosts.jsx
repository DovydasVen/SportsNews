import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import api from "../api/axios";

export default function CategoryPosts() {
  const { categoryId } = useParams();

  const [posts, setPosts] = useState([]);
  const [categoryName, setCategoryName] = useState("");

  const [title, setTitle] = useState("");
  const [text, setText] = useState("");

  const [showCreate, setShowCreate] = useState(false);

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
    });

    setTitle("");
    setText("");
    setShowCreate(false);
    load();
  };

  return (
    <div className="page-container">
      <Link to="/" className="text-decoration-none mb-2 d-inline-flex align-items-center" >
        <i className="fa-solid fa-chevron-left me-1"></i> Grįžti atgal
      </Link>

      <h2 className="mb-3">{categoryName}</h2>

      {/* CREATE POST SECTION */}
      {isLoggedIn && (
        <>
          {!showCreate && (
            <button
              className="btn btn-primary btn-pill mb-3"
              onClick={() => setShowCreate(true)}
            >
              Sukurti įrašą
            </button>
          )}

          {showCreate && (
            <div className="card-forum mb-4">
              <div className="d-flex justify-content-between align-items-center mb-2">
                <h5 className="mb-0">Kurti naują įrašą</h5>

                <button
                  className="btn btn-sm btn-outline-light btn-pill"
                  onClick={() => setShowCreate(false)}
                >
                  Atšaukti
                </button>
              </div>

              <form onSubmit={createPost}>
                <div className="mb-2">
                  <input
                    className="form-control"
                    placeholder="Pavadinimas"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    required
                  />
                </div>

                <div className="mb-2">
                  <textarea
                    className="form-control"
                    rows={3}
                    placeholder="Tekstas"
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                    required
                  />
                </div>

                <button className="btn btn-success btn-pill" type="submit">
                  Paskelbti
                </button>
              </form>
            </div>
          )}
        </>
      )}

      {/* POSTS LIST */}
      {posts.map((p) => (
        <Link
          key={p.id}
          to={`/categories/${categoryId}/posts/${p.id}`}
          className="card-forum d-block"
        >
          <h5 className="mb-1">{p.title}</h5>

          <p className="mb-1" style={{ color: "#d1d5db" }}>
            {p.text.length > 140 ? p.text.slice(0, 140) + "..." : p.text}
          </p>
        </Link>
      ))}

      {posts.length === 0 && (
        <p className="text-muted">Įrašų šioje kategorijoje nėra</p>
      )}
    </div>
  );
}