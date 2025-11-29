from django.urls import path
from .api_views import BlogPostListAPIView, BlogPostDetailAPIView

urlpatterns = [
    path("posts/", BlogPostListAPIView.as_view(), name="posts-list"),
    path("posts/<slug:slug>/", BlogPostDetailAPIView.as_view(), name="posts-detail"),
]
