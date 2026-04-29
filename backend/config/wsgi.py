"""
Django backend WSGI application.

This file exposes the synchronous server gateway application for WSGI
servers that run the backend project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()

# File History
# 2026-04-29: Added backend WSGI application header and footer.
# 2026-04-29: Updated settings module reference from app to config.
