import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import api from "../api/axios";
import RoleGuard from "../components/RoleGuard";

export default function Categories() {
  const [categories, setCategories] = useState([]);
  const [name, setName] = useState("");

  const load = async () => {
    const res = await api.get("/api/categories");
    setCategories(res.data);
  };

  useEffect(() => {
    load();
  }, []);

  const createCategory = async (e) => {
    e.preventDefault();
    if (!name.trim()) return;
    await api.post("/api/categories", { name });
    setName("");
    load();
  };

  return (
    <div className="page-container">

      <RoleGuard allowed={["EDITOR", "ADMIN"]}>
        <div className="card-forum mb-4">
          <h5 className="mb-2">Sukurti kategorija</h5>
          <form onSubmit={createCategory} className="d-flex gap-2">
            <input
              className="form-control"
              placeholder="Category name"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
            <button className="btn btn-primary btn-pill" type="submit">
              Add
            </button>
          </form>
        </div>
      </RoleGuard>

      {categories.map((c) => (
        <Link
          key={c.id}
          to={`/categories/${c.id}`}
          className="card-forum d-flex justify-content-between align-items-center"
        >
          <div>
            <h5 className="mb-1">{c.name}</h5>
            <small style={{ color: "#9ca3af" }}>
            </small>
          </div>
          <i className="fa-solid fa-chevron-right"></i>
        </Link>
      ))}

      {categories.length === 0 && (
        <p className="text-muted">No categories yet.</p>
      )}
    </div>
  );
}
