from .serializers import UserSerializer, PostSerializers, PhotoSerializer
from .models import User, Post, Photo
from rest_framework import generics, permissions
# Create your views here.


class UserList(generics.ListCreateAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class UserDetail(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer
    lookup_field = 'username'


class PostList(generics.ListCreateAPIView):
    model = Post
    serializer_class = PostSerializers
    permission_classes = [
        permissions.AllowAny
    ]


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Post
    serializer_class = PostSerializers
    permission_classes = [
        permissions.AllowAny
    ]


class UserPostList(generics.ListAPIView):
    model = Post
    serializer_class = PostSerializers
    def get_queryset(self):
        queryset = super(UserPostList, self).get_queryset()
        return  queryset.filter(author__username=self.kwargs.get('username'))


class PhotoList(generics.ListCreateAPIView):
    model = Photo
    serializer_class = PhotoSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Photo
    serializer_class = PhotoSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class PostPhotoList(generics.ListAPIView):
    model = Photo
    serializer_class = PhotoSerializer

    def get_queryset(self):
        queryset = super(PostPhotoList,self).get_queryset()
        return queryset.filter(post__pk=self.kwargs.get('pk'))