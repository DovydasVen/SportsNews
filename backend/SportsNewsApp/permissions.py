from rest_framework.permissions import BasePermission, SAFE_METHODS
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiResponse, OpenApiExample

UNAUTHORIZED_RESPONSE = {
    401: OpenApiResponse(
        description="Authentication credentials are missing or invalid",
        response=OpenApiTypes.OBJECT,
        examples=[
            OpenApiExample(
                "Unauthorized",
                value={"detail": "Authentication credentials were not provided."}
            )
        ]
    )
}

FORBIDDEN_RESPONSE = {
    403: OpenApiResponse(
        description="You do not have permission to perform this action",
        response=OpenApiTypes.OBJECT,
        examples=[
            OpenApiExample(
                "Forbidden",
                value={"detail": "You do not have permission to perform this action."}
            )
        ]
    )
}

class IsEditorOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or (request.user.is_authenticated and request.user.role in ["EDITOR", "ADMIN"])
        )

class IsOwnerOrEditorOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if not request.user.is_authenticated:
            return False

        if getattr(request.user, "role", None) in ["ADMIN", "EDITOR"]:
            return True
        
        return hasattr(obj, "author_id") and obj.author_id == request.user.id