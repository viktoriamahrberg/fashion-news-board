from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget


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
        fields = (
            'title', 'content', 'featured_image', 'excerpt',
            'original_news_link'
            )
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Required'
                }),
            'content': SummernoteWidget(),
            'featured_image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
                }),
            'excerpt': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Required'
                }),
            'original_news_link': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Required'
                }),
        }


class EditPostForm(forms.ModelForm):
    """
    Editing posts
    """
    class Meta:
        model = Post
        fields = ('title', 'content', 'excerpt', 'original_news_link')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Required'
                }),
            'content': SummernoteWidget(),
            'excerpt': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Required'
                }),
            'original_news_link': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Required'
                }),
        }
