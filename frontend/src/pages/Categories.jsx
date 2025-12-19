import { useEffect, useState } from "react";
import api from "../api/axios";

export default function Categories() {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    api.get("/api/categories")
       .then(res => setCategories(res.data))
       .catch(() => alert("Nepavyko gauti kategorijų"));
  }, []);

  return (
    <div className="container mt-4">
      <h2>Categories</h2>

      <ul className="list-group">
        {categories.map(c => (
          <li key={c.id} className="list-group-item">
            {c.name}
          </li>
        ))}
      </ul>
    </div>
  );
}
