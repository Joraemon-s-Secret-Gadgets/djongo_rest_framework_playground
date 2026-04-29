"""
Blog API app configuration.

This file defines the Django application configuration for the API app.
"""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"

# File History
# 2026-04-29: Added API app configuration header and footer.
