from django.db import models
from sportsnews import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=64)
    text = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.title + " " + self.text

class Comment(models.Model):
    text = models.CharField(max_length=500)
    Post = models.ForeignKey(Post, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.headline