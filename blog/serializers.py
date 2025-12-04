from rest_framework import serializers
from .models import BlogPage


class BlogPostSerializer(serializers.ModelSerializer):
    """
    Serializer for BlogPage to expose blog posts via REST API.
    
    Returns blog post metadata including auto-generated intro from
    search_description or first 200 characters of markdown body.
    """
    intro = serializers.SerializerMethodField()

    class Meta:
        model = BlogPage
        fields = ["id", "title", "slug", "date", "intro"]

    def get_intro(self, obj):
        """
        Extract intro text from search_description or markdown body.
        
        Returns:
            str: Introduction text (max 200 characters) with markdown stripped
        """
        if obj.search_description:
            return obj.search_description
        
        # Get plain text from markdown body
        if obj.body:
            import re
            # Strip markdown syntax (links, emphasis, headers, etc.)
            plain_text = re.sub(r'[#*`\[\]()]', '', str(obj.body))
            return plain_text[:200].strip()
        return ""
