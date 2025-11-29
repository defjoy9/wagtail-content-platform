from rest_framework import generics
from .models import BlogPage
from .serializers import BlogPostSerializer


class BlogPostListAPIView(generics.ListAPIView):
    """
    API endpoint that returns a list of all published blog posts.
    """
    queryset = BlogPage.objects.live().order_by("-date")
    serializer_class = BlogPostSerializer


class BlogPostDetailAPIView(generics.RetrieveAPIView):
    """
    API endpoint that returns a single blog post by slug.
    """
    queryset = BlogPage.objects.live()
    lookup_field = "slug"
    serializer_class = BlogPostSerializer
