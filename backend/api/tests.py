"""
Blog API tests.

This file verifies health check behavior and blog post CRUD endpoints for the
API app.
"""

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Post


class BlogAPITest(APITestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title="test title",
            content="test content",
            is_active=True,
        )

    def test_root_health_check(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "healthy")

    def test_get_blog_list(self):
        response = self.client.get("/blog/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_blog(self):
        payload = {
            "title": "new post",
            "content": "new content",
            "is_active": True,
        }

        response = self.client.post("/blog/", payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_get_single_blog(self):
        response = self.client.get(f"/blog/{self.post.id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "test title")

    def test_update_blog(self):
        payload = {
            "title": "updated title",
            "content": "updated content",
            "is_active": True,
        }

        response = self.client.put(
            f"/blog/{self.post.id}/",
            payload,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.post.refresh_from_db()

        self.assertEqual(self.post.title, "updated title")

    def test_delete_blog(self):
        response = self.client.delete(f"/blog/{self.post.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)

# File History
# 2026-04-29: Added blog API test header and footer.
