import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios";

export default function Login() {
  const [username, setU] = useState("");
  const [password, setP] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const login = async (e) => {
    e.preventDefault();
    setError("");
    try {
      const res = await api.post("/api/login/", { username, password });
      localStorage.setItem("access", res.data.access);
      localStorage.setItem("refresh", res.data.refresh);
      localStorage.setItem("role", res.data.role);
      localStorage.setItem("username", res.data.username);
      navigate("/");
    } catch (err) {
      setError("Neteisingas vartotojo vardas arba slaptažodis");
    }
  };

  return (
    <div className="page-container">
      <div className="card-forum" style={{ maxWidth: 420, margin: "2rem auto" }}>
        <h2 className="mb-3">Prisijungti</h2>
        {error && <div className="alert alert-danger">{error}</div>}

        <form onSubmit={login}>
          <div className="mb-3">
            <label className="form-label">Slapyvardis</label>
            <input
              className="form-control"
              value={username}
              onChange={(e) => setU(e.target.value)}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Slaptažodis</label>
            <input
              type="password"
              className="form-control"
              value={password}
              onChange={(e) => setP(e.target.value)}
              required
            />
          </div>

          <button type="submit" className="btn btn-primary w-100 btn-pill">
            Login
          </button>
        </form>
      </div>
    </div>
  );
}
