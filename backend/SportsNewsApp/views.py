from django.forms import ValidationError
from django.shortcuts import render
from django.http import JsonResponse
from sportsnews.settings import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from rest_framework.permissions import AllowAny
from .models import *
from .serializers import *
from .permissions import *

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
        **UNAUTHORIZED_RESPONSE,
        **FORBIDDEN_RESPONSE,
    },
)


@api_view(['GET', 'POST'])
@permission_classes([IsEditorOrAdmin])
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
        **UNAUTHORIZED_RESPONSE,
        **FORBIDDEN_RESPONSE,
    },
)

@extend_schema(
    methods=['DELETE'],
    responses={
        204: OpenApiTypes.NONE,
        404: OpenApiTypes.NONE,        
        **UNAUTHORIZED_RESPONSE,
        **FORBIDDEN_RESPONSE,
    },
)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsEditorOrAdmin])
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
    responses={
        200: PostSerializer(many=True)
    },
)

@extend_schema(
    methods=['POST'],
    request=PostSerializer,
    responses={
        201: PostSerializer,
        400: OpenApiTypes.OBJECT,
        **UNAUTHORIZED_RESPONSE,
        **FORBIDDEN_RESPONSE,
    },
)

@api_view(['GET', 'POST'])
@permission_classes([IsOwnerOrEditorOrAdmin])
def postListApi(request, id=None):
    if request.method == "GET":
        posts = Post.objects.filter(category_id=id)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author = request.user, category=Category.objects.get(pk=id))
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
        **UNAUTHORIZED_RESPONSE,
        **FORBIDDEN_RESPONSE,
    },
)

@extend_schema(
    methods=['DELETE'],
    responses={
        204: OpenApiTypes.NONE,
        404: OpenApiTypes.NONE,
        **UNAUTHORIZED_RESPONSE,
        **FORBIDDEN_RESPONSE,
    },
)

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsOwnerOrEditorOrAdmin])
def postDetailApi(request, id=None, id2=None):
    try:
        post = Post.objects.filter(category_id=id).get(pk=id2)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    checker = IsOwnerOrEditorOrAdmin()

    if request.method in ["PUT", "DELETE"]:
        if not checker.has_object_permission(request, None, post):
            return Response({"detail": "You do not have permission to perform this action."},
                            status=status.HTTP_403_FORBIDDEN)

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
        **UNAUTHORIZED_RESPONSE,
        **FORBIDDEN_RESPONSE,
    },
)

@api_view(['GET','POST'])
@permission_classes([IsOwnerOrEditorOrAdmin])
def commentListApi(request, id=None, id2=None):
    if request.method == "GET":
        comments = Comment.objects.filter(post_id=id2)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                author=request.user,
                post=Post.objects.get(pk=id2)
            )
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
        **UNAUTHORIZED_RESPONSE,
        **FORBIDDEN_RESPONSE,
    },
)

@extend_schema(
    methods=['DELETE'],
    responses={
        204: OpenApiTypes.NONE,
        404: OpenApiTypes.NONE,
        **UNAUTHORIZED_RESPONSE,
        **FORBIDDEN_RESPONSE,
    },
)


@api_view(['GET','PUT','DELETE'])
@permission_classes([IsOwnerOrEditorOrAdmin])
def commentDetailApi(request, id=None, id2=None, id3=None):
    try:
        comment = Comment.objects.filter(post_id=id2).get(pk=id3)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    checker = IsOwnerOrEditorOrAdmin()

    if request.method in ["PUT", "DELETE"]:
        if not checker.has_object_permission(request, None, comment):
            return Response({"detail": "You do not have permission to perform this action."},
                            status=status.HTTP_403_FORBIDDEN)

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
    
@extend_schema(
    request=CustomTokenSerializer,
    responses={200: LoginResponseSerializer},
    description="Login – returns access and refresh tokens"
)
class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer

@extend_schema(
    request=RegisterSerializer,
    responses={201: RegisterSerializer},
    description="Registers new USER account"
)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_api(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()

        return Response( {"user": { "id": user.id, "username": user.username, "email": user.email, "role": user.role}},
            status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)