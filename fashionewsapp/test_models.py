from django.test import TestCase
from .models import Post


class TestPost(TestCase):

    def create_post(self, title="only a test"):
        return Post.objects.create(title=title)

    def test_post(self):
        post = self.create_post()
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.__str__(), post.title)
