from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import *


class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "role", "is_staff", "is_superuser")
    fieldsets = UserAdmin.fieldsets + (
        ("Role", {"fields": ("role",)}),
    )

admin.site.register(User, CustomUserAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "author")
    search_fields = ("title", "text")
    list_filter = ("category", "author")
    
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "post", "author")
    search_fields = ("text",)
    list_filter = ("author", "post")

admin.site.register(Comment, CommentAdmin)