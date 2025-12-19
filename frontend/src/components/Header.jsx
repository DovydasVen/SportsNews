import { useState, useEffect } from "react";
import { Link, useNavigate, useLocation } from "react-router-dom";

export default function Header() {
  const [open, setOpen] = useState(false);
  const [username, setUsername] = useState(null);
  const [role, setRole] = useState(null);
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    setUsername(localStorage.getItem("username"));
    setRole(localStorage.getItem("role"));
  }, [location.key]); // atsinaujina po login/logout

  const logout = () => {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    localStorage.removeItem("role");
    localStorage.removeItem("username");
    navigate("/login");
  };

  return (
    <header className="header">
      <div className="header-inner">
        <Link to="/" className="logo">
          <span>Sports Forum</span>
        </Link>

        <button
          className="hamburger"
          onClick={() => setOpen((o) => !o)}
          aria-label="Toggle navigation"
        >
          <i className="fa-solid fa-bars"></i>
        </button>

        <nav className={`nav-links ${open ? "open" : ""}`}>
          {username ? (
            <>
              <div className="user-pill">
                <i className="fa-regular fa-user"></i>
                <span>{username}</span>
                <span style={{ fontSize: "0.75rem", opacity: 0.7 }}>
                  ({role})
                </span>
              </div>
              <button
                className="btn btn-sm btn-outline-light btn-pill"
                onClick={logout}
              >
                Atsijungti
              </button>
            </>
          ) : (
            <>
              <Link
                className="nav-link"
                to="/login"
                onClick={() => setOpen(false)}
              >
                Login
              </Link>
              <Link
                className="nav-link nav-link-primary"
                to="/register"
                onClick={() => setOpen(false)}
              >
                Register
              </Link>
            </>
          )}
        </nav>
      </div>
    </header>
  );
}
