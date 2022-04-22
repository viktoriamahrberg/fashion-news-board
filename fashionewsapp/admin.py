from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Managing post in the Admin Panel
    """
    list_display = ('title', 'slug', 'date_published', 'author')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    list_filter = ('date_published',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Managing comments in the Admin Panel
    """
    list_display = ('post', 'body', 'name', 'date_published')
    search_fields = ('name', 'body')
    list_filter = ('name',)
    
