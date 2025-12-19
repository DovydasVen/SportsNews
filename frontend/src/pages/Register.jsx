import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios";

export default function Register() {
  const [username, setU] = useState("");
  const [email, setE] = useState("");
  const [password, setP] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const register = async (e) => {
    e.preventDefault();
    setError("");
    try {
      await api.post("/api/register/", { username, email, password });
      navigate("/login");
    } catch (err) {
      setError("Registracija nepavyko (patikrink laukus ar ar vartotojas unikalus).");
    }
  };

  return (
    <div className="page-container">
      <div className="card-forum" style={{ maxWidth: 420, margin: "2rem auto" }}>
        <h2 className="mb-3">Register</h2>
        {error && <div className="alert alert-danger">{error}</div>}

        <form onSubmit={register}>
          <div className="mb-3">
            <label className="form-label">Username</label>
            <input
              className="form-control"
              value={username}
              onChange={(e) => setU(e.target.value)}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Email</label>
            <input
              type="email"
              className="form-control"
              value={email}
              onChange={(e) => setE(e.target.value)}
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Password</label>
            <input
              type="password"
              className="form-control"
              value={password}
              onChange={(e) => setP(e.target.value)}
              required
            />
          </div>

          <button type="submit" className="btn btn-success w-100 btn-pill">
            Create account
          </button>
        </form>
      </div>
    </div>
  );
}
