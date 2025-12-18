from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsEditorOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or (request.user.is_authenticated and request.user.role in ["EDITOR", "ADMIN"])
        )

class IsOwnerOrEditorOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        # safe requests allowed
        if request.method in SAFE_METHODS:
            return True

        # must be logged in
        if not request.user.is_authenticated:
            return False

        # admins + editors can do everything
        if request.user.role in ["ADMIN", "EDITOR"]:
            return True

        # user can edit only own posts
        return hasattr(obj, "author_id") and obj.author_id == request.user.id