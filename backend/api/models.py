"""
Blog API models.

This file defines database models for blog post resources used by the API app.
"""

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """게시글 제목 반환"""
        return self.title

# File History
# 2026-04-29: Added blog API model header and footer.
