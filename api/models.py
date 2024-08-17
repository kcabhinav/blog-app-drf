from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length = 100, default='', blank=False, null=False)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
