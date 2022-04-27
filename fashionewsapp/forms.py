from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget



class CommentForm(forms.ModelForm):
    """
    Adding comments to posts
    """
    class Meta:
        model = Comment
        fields = ('body',)



class AddPostForm(forms.ModelForm):
    """
    Creating new posts
    """
    class Meta:
        model = Post
        fields = ('title', 'author', 'content', 'featured_image', 'excerpt', 'original_news_link')
        widgets = {
            'content': SummernoteWidget(),
        }
    
class EditPostForm(forms.ModelForm):
    """
    Editing posts
    """
    class Meta:
        model = Post
        fields = ('title', 'content', 'excerpt', 'original_news_link')
        widgets = {
            'content': SummernoteWidget(attrs={'width': '50%'}),
        }
       


