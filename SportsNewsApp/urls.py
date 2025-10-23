from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    # API URLs
    #Category
    path("api/categories", views.categoryApi, name="categoryList"),
    path("api/categories/<int:id>", views.categoryApi, name="categoryById"),

    #Post
    path("api/categories/<int:id>/posts", views.postApi, name="postList"),
    path("api/categories/<int:id>/posts/<int:id2>", views.postApi, name="postById"),

    #Comments
    path("api/categories/<int:id>/posts/<int:id2>/comments", views.commentApi, name="commentList"),
    path("api/categories/<int:id>/posts/<int:id2>/comments/<int:id3>", views.commentApi, name="commentById"),
]