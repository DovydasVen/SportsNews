from django.urls import path
from . import views

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
]