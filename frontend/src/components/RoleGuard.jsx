export default function RoleGuard({ allowed, children }) {
  const role = localStorage.getItem("role");
  if (!role) return null;
  if (!allowed.includes(role)) return null;
  return children;
}
