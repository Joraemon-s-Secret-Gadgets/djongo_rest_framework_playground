"""
Blog API serializers.

This file defines request and response serialization for blog post resources.
"""

from rest_framework import serializers

from .models import Post


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

# File History
# 2026-04-29: Added blog API serializer header and footer.
