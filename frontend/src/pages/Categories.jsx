import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import api from "../api/axios";
import RoleGuard from "../components/RoleGuard";
import ConfirmModal from "../components/ConfirmModal";

export default function Categories() {
  const [categories, setCategories] = useState([]);
  const [name, setName] = useState("");

  const [showCreate, setShowCreate] = useState(false);

  const [showDelete, setShowDelete] = useState(false);
  const [deleteId, setDeleteId] = useState(null);
  const [deleteName, setDeleteName] = useState("");

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
    setShowCreate(false);
    load();
  };

  const deleteCategory = async () => {
    if (!deleteId) return;
    await api.delete(`/api/categories/${deleteId}`);
    setDeleteId(null);
    setDeleteName("");
    setShowDelete(false);
    load();
  };

  return (
    <div className="page-container">
      <h2 className="mb-3">Kategorijos</h2>

      {/* CREATE CATEGORY */}
      <RoleGuard allowed={["EDITOR", "ADMIN"]}>
        {!showCreate && (
          <button
            className="btn btn-primary btn-pill mb-3"
            onClick={() => setShowCreate(true)}
          >
            Sukurti kategoriją
          </button>
        )}

        {showCreate && (
          <div className="card-forum mb-4">
            <div className="d-flex justify-content-between align-items-center mb-2">
              <h5 className="mb-0">Nauja kategorija</h5>

              <button
                className="btn btn-sm btn-outline-light btn-pill"
                onClick={() => setShowCreate(false)}
              >
                Atšaukti
              </button>
            </div>

            <form onSubmit={createCategory}>
              <div className="mb-2">
                <input
                  className="form-control"
                  placeholder="Kategorijos pavadinimas"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  required
                />
              </div>

              <button className="btn btn-success btn-pill" type="submit">
                Sukurti
              </button>
            </form>
          </div>
        )}
      </RoleGuard>

      {/* CATEGORY LIST */}
      {categories.map((c) => (
        <div
          key={c.id}
          className="card-forum d-flex justify-content-between align-items-center"
        >
          <Link
            to={`/categories/${c.id}`}
            className="flex-grow-1 text-decoration-none"
          >
            <h5 className="mb-1">{c.name}</h5>
          </Link>

          <RoleGuard allowed={["EDITOR", "ADMIN"]}>
            <button
              className="btn btn-danger btn-pill ms-3"
              onClick={() => {
                setDeleteId(c.id);
                setDeleteName(c.name);
                setShowDelete(true);
              }}
            >
              Ištrinti
            </button>
          </RoleGuard>
        </div>
      ))}

      {categories.length === 0 && (
        <p className="text-muted">Kategorijų kol kas nėra.</p>
      )}

      {/* CONFIRM DELETE MODAL */}
      <ConfirmModal
        show={showDelete}
        title="Ištrinti kategoriją"
        text={
          deleteName
            ? `Ar tikrai norite ištrinti kategoriją "${deleteName}"?`
            : "Ar tikrai norite ištrinti šią kategoriją?"
        }
        onConfirm={deleteCategory}
        onClose={() => setShowDelete(false)}
      />
    </div>
  );
}
