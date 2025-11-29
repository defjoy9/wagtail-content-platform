from rest_framework import serializers
from .models import BlogPage


class BlogPostSerializer(serializers.ModelSerializer):
    """
    Serializer for BlogPage to expose blog posts via REST API.
    """
    intro = serializers.SerializerMethodField()

    class Meta:
        model = BlogPage
        fields = ["id", "title", "slug", "date", "intro"]

    def get_intro(self, obj):
        """
        Extract intro from search_description or body content.
        """
        if obj.search_description:
            return obj.search_description
        # Strip HTML and get first 200 chars from body
        from wagtail.rich_text import RichText
        if obj.body:
            plain_text = obj.body.source if hasattr(obj.body, 'source') else str(obj.body)
            # Basic HTML stripping
            import re
            plain_text = re.sub('<[^<]+?>', '', plain_text)
            return plain_text[:200].strip()
        return ""
