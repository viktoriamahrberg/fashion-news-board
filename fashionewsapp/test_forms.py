from django.test import TestCase
from .forms import AddPostForm

class TestAddPostForm(TestCase):

    def test_item_title_is_required(self):
        form = AddPostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')


  
