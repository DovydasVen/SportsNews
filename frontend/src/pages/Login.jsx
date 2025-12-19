import { useState } from "react";
import api from "../api/axios";

export default function Login() {
  const [username, setU] = useState("");
  const [password, setP] = useState("");
  const [error, setError] = useState("");

  const login = async () => {
    try {
      const res = await api.post("/api/login/", {
        username,
        password
      });

      localStorage.setItem("access", res.data.access);
      localStorage.setItem("refresh", res.data.refresh);
      localStorage.setItem("role", res.data.role);
      window.location.href = "/";
    } catch (e) {
      setError("Neteisingi duomenys");
    }
  };

  return (
    <div className="container mt-5">
      <h2>Login</h2>

      {error && <div className="alert alert-danger">{error}</div>}

      <input
        className="form-control mb-2"
        placeholder="Username"
        onChange={(e) => setU(e.target.value)}
      />

      <input
        className="form-control mb-2"
        placeholder="Password"
        type="password"
        onChange={(e) => setP(e.target.value)}
      />

      <button className="btn btn-primary" onClick={login}>
        Login
      </button>
    </div>
  );
}
