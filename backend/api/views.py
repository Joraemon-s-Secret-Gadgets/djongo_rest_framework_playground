"""
Blog API views.

This file handles health check responses and blog post CRUD API requests
through Django REST Framework view functions and viewsets.
"""

from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import serializers, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializers


@extend_schema(
    responses=inline_serializer(
        name="RootResponse",
        fields={
            "status": serializers.CharField(),
            "service": serializers.CharField(),
            "message": serializers.CharField(),
        },
    ),
)
@api_view(["GET"])
def root(request):
    return Response(
        {
            "status": "healthy",
            "service": "django-rest-framework",
            "message": "welcome to django rest framework",
        },
        status=status.HTTP_200_OK,
    )


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializers


# File History
# 2026-04-29: Added blog API views header and footer.
