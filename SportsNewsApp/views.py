from django.forms import ValidationError
from django.shortcuts import render
from django.http import JsonResponse
from sportsnews.settings import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from .models import *
from .serializers import *

def index(request):
    context = {}
    return render(request, "pages/index.html", context=context)

@api_view(['GET','POST','PUT',"DELETE"])
def categoryApi(request, id=None):
    if request.method == "GET":
        if id:
            try:
                category = Category.objects.get(pk=id)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        else:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many = True)
            return Response({'categories:': serializer.data})
        
    elif request.method == "POST":
        serializer =  CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
    elif request.method == "PUT":
        try:
            category = Category.objects.get(pk=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category, data = request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == "DELETE":
        try:
            category = Category.objects.get(pk=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST','PUT',"DELETE"])
def postApi(request, id=None, id2=None):
    if request.method == "GET":
        if id and id2:
            try:
                post = Post.objects.filter(category_id = id).get(pk=id2)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        
        else:
            posts = Post.objects.filter(category_id = id)
            serializer = PostSerializer(posts, many = True)
            return Response({'posts:': serializer.data})
        
    elif request.method == "POST":
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "PUT":
        try:
            post = Post.objects.get(pk=id2)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post, data = request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        try:
            post = Post.objects.get(pk=id2)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST','PUT',"DELETE"])
def commentApi(request, id=None, id2=None, id3=None):
    if request.method == "GET":
        if id and id2 and id3:
            try:
                comment = Comment.objects.filter(post_id = id2).get(pk=id3)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        
        else:
            comments = Comment.objects.filter(post_id = id2)
            serializer = CommentSerializer(comments, many = True)
            return Response({'comments:': serializer.data})
        
    elif request.method == "POST":
        serializer =  CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        try:
            comment = Comment.objects.get(pk=id3)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(comment, data = request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            
    elif request.method == "DELETE":
        try:
            comment = Comment.objects.get(pk=id3)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)