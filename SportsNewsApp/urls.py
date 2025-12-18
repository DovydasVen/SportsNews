from django.urls import path
from . import views
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from SportsNewsApp.serializers import CustomTokenSerializer


@extend_schema(
    request=CustomTokenSerializer,
    responses={200: CustomTokenSerializer},
    description="Login – grąžina access ir refresh tokenus su role"
)
class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer


urlpatterns = [
    path("", views.index, name="index"),

    # API URLs
    # Category
    path("api/categories", views.categoryListApi),
    path("api/categories/<int:id>", views.categoryDetailApi),

    #Posts
    path("api/categories/<int:id>/posts", views.postListApi),
    path("api/categories/<int:id>/posts/<int:id2>", views.postDetailApi),

    #Comments
    path("api/categories/<int:id>/posts/<int:id2>/comments", views.commentListApi),
    path("api/categories/<int:id>/posts/<int:id2>/comments/<int:id3>", views.commentDetailApi),

    path("api/register/", views.register_api, name="register"),
    path("api/login/", views.CustomTokenView.as_view(), name="token_obtain_pair"),
    path("api/refresh/", views.CustomRefreshView.as_view(), name="token_refresh"),
]