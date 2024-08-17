from rest_framework import serializers
from .models import Post, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    author = serializers.ReadOnlyField(source='author.name')
    class Meta:
        model = Post
        fields = '__all__'
