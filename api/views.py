from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.mixins import DestroyModelMixin, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer, AuthorSerializer

from .models import Post, Author
# Create your views here.

class PostListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
