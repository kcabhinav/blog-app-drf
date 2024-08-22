from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import PostSerializer, AuthorSerializer

from .models import Post, Author
# Create your views here.

# class PostListView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # Adding an extra action to get the author of a post
    @action(detail=True, methods=['get'], url_path='get_author')
    def get_post_author(self, request, pk=None):
            post = self.get_object()
            author = post.author
            serializer = AuthorSerializer(author)
            return Response(serializer.data)

# class AuthorListView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# class AuthorView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # Adding an extra action to get the posts of an author
    @action(detail=True, methods=['get'], url_path='get_posts')
    def get_author_posts(self, request, pk=None):
            author = self.get_object()
            posts = author.post_set.all()
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)
