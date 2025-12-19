import axios from "axios";

const api = axios.create({
  baseURL: "https://sportsnewssite-api.vercel.app/",
});

// Jei turim token, automatiškai dedam į header
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("access");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
