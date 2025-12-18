from django.db import models
from sportsnews import settings
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=64)
    text = models.CharField(max_length=512)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.title + " " + self.text

class Comment(models.Model):
    text = models.CharField(max_length=512)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.text

class User(AbstractUser):
    ROLE_CHOICES = (
        ("USER", "User"),
        ("EDITOR", "Editor"),
        ("ADMIN", "Admin"),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="USER")

    def __str__(self):
        return self.username