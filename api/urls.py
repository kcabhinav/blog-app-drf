from django.urls import path
from .views import PostView, PostListView, AuthorListView, AuthorView, api_root
urlpatterns = [
    path('', api_root, name='api_root'),
    path('post/', PostListView.as_view(), name = 'post_list_view'),
    path('post/<int:pk>', PostView.as_view(), name = 'post_view'),
    path('author/', AuthorListView.as_view(), name = 'author_list_view'),
    path('author/<int:pk>', AuthorView.as_view(), name = 'author_view'),
]
