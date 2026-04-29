#!/usr/bin/env python3
"""
Django management command entrypoint.

This file routes command-line administrative tasks to the project settings
module used by the backend application.
"""

import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

# File History
# 2026-04-29: Added backend Django management entrypoint header and footer.
# 2026-04-29: Updated settings module reference from app to config.
