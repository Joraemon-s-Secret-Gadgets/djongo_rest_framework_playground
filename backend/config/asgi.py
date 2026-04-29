"""
Django backend ASGI application.

This file exposes the asynchronous server gateway application for ASGI
servers that run the backend project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_asgi_application()

# File History
# 2026-04-29: Added backend ASGI application header and footer.
# 2026-04-29: Updated settings module reference from app to config.
