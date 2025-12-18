from django.forms import ValidationError
from django.shortcuts import render
from django.http import JsonResponse
from sportsnews.settings import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from .models import *
from .serializers import *

def index(request):
    context = {}
    return render(request, "pages/index.html", context=context)

@extend_schema(
    methods=['GET'],
    responses={200: CategorySerializer(many=True)},
)

@extend_schema(
    methods=['POST'],
    request=CategorySerializer,
    responses={
        201: CategorySerializer,
        400: OpenApiTypes.OBJECT,
    },
)
@api_view(['GET', 'POST'])
def categoryListApi(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    methods=['GET'],
    parameters=[OpenApiParameter("id", int, location=OpenApiParameter.PATH)],
    responses={
        200: CategorySerializer,
        404: OpenApiTypes.NONE,
    },
)

@extend_schema(
    methods=['PUT'],
    request=CategorySerializer,
    responses={
        200: CategorySerializer,
        400: OpenApiTypes.OBJECT,
        404: OpenApiTypes.NONE,
    },
)

@extend_schema(
    methods=['DELETE'],
    responses={
        204: OpenApiTypes.NONE,
        404: OpenApiTypes.NONE,
    },
)

@api_view(['GET', 'PUT', 'DELETE'])
def categoryDetailApi(request, id=None):
    try:
        category = Category.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return Response(CategorySerializer(category).data)

    elif request.method == "PUT":
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@extend_schema(
    methods=['GET'],
    parameters=[OpenApiParameter("id", int, location=OpenApiParameter.PATH)],
    responses={200: PostSerializer(many=True)},
)

@extend_schema(
    methods=['POST'],
    request=PostSerializer,
    responses={
        201: PostSerializer,
        400: OpenApiTypes.OBJECT,
    },
)

@api_view(['GET', 'POST'])
def postListApi(request, id=None):
    if request.method == "GET":
        posts = Post.objects.filter(category_id=id)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    methods=['GET'],
    parameters=[
        OpenApiParameter("id", int, location=OpenApiParameter.PATH),
        OpenApiParameter("id2", int, location=OpenApiParameter.PATH),
    ],
    responses={
        200: PostSerializer,
        404: OpenApiTypes.NONE,
    },
)

@extend_schema(
    methods=['PUT'],
    request=PostSerializer,
    responses={
        200: PostSerializer,
        400: OpenApiTypes.OBJECT,
        404: OpenApiTypes.NONE,
    },
)

@extend_schema(
    methods=['DELETE'],
    responses={
        204: OpenApiTypes.NONE,
        404: OpenApiTypes.NONE,
    },
)
@api_view(['GET','PUT','DELETE'])
def postDetailApi(request, id=None, id2=None):
    try:
        post = Post.objects.filter(category_id=id).get(pk=id2)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return Response(PostSerializer(post).data)

    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@extend_schema(
    methods=['GET'],
    parameters=[
        OpenApiParameter("id", int, location=OpenApiParameter.PATH),
        OpenApiParameter("id2", int, location=OpenApiParameter.PATH),
    ],
    responses={200: CommentSerializer(many=True)},
)

@extend_schema(
    methods=['POST'],
    request=CommentSerializer,
    responses={
        201: CommentSerializer,
        400: OpenApiTypes.OBJECT,
    },
)
@api_view(['GET','POST'])
def commentListApi(request, id=None, id2=None):
    if request.method == "GET":
        comments = Comment.objects.filter(post_id=id2)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    methods=['GET'],
    parameters=[
        OpenApiParameter("id", int, location=OpenApiParameter.PATH),
        OpenApiParameter("id2", int, location=OpenApiParameter.PATH),
        OpenApiParameter("id3", int, location=OpenApiParameter.PATH),
    ],
    responses={
        200: CommentSerializer,
        404: OpenApiTypes.NONE,
    },
)

@extend_schema(
    methods=['PUT'],
    request=CommentSerializer,
    responses={
        200: CommentSerializer,
        400: OpenApiTypes.OBJECT,
        404: OpenApiTypes.NONE,
    },
)

@extend_schema(
    methods=['DELETE'],
    responses={
        204: OpenApiTypes.NONE,
        404: OpenApiTypes.NONE,
    },
)
@api_view(['GET','PUT','DELETE'])
def commentDetailApi(request, id=None, id2=None, id3=None):
    try:
        comment = Comment.objects.filter(post_id=id2).get(pk=id3)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return Response(CommentSerializer(comment).data)

    elif request.method == "PUT":
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)