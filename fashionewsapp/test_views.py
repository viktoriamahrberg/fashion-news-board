from django.test import TestCase
from .views import PostList, CreatePost
from .models import Post


class TestViews(TestCase):

    def test_post_list_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')

    def test_edit_post_page(self):
        response = self.client.get('/add_post')
        self.assertTemplateUsed(response, 'add_post.html')