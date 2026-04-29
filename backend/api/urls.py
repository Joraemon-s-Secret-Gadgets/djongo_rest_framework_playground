"""
Blog API URL configuration.

This file connects the API root endpoint and blog router routes for the
backend application.
"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BlogViewSet, root

router = DefaultRouter()
router.register("blog", BlogViewSet, basename="blog")

urlpatterns = [path("", root), path("", include(router.urls))]

# File History
# 2026-04-29: Added blog API URL configuration header and footer.
