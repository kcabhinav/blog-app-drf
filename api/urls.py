from django.urls import path
from .views import PostViewSet, AuthorViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

router = SimpleRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'authors', AuthorViewSet, basename='author')


urlpatterns = router.urls
