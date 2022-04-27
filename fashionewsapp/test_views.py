from django.test import TestCase
from .views import PostList, CreatePost
from .models import Post


class TestViews(TestCase):

    def test_post_list_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')
