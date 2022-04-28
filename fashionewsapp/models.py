from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify
from django.urls import reverse


class Post(models.Model):
    """
    Post Model
    """
    title = models.CharField(max_length=200, unique=True, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="news_post"
        )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=False)
    featured_image = CloudinaryField('image', default='news_image', blank=True)
    excerpt = models.TextField(blank=False)
    date_published = models.DateTimeField(auto_now_add=True)
    original_news_link = models.URLField(blank=False, null=True)

    class Meta:
        """
        Order newest post first
        """
        ordering = ['date_published']

    def __str__(self):
        return self.title

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Post, self).save()

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.slug)])


class Comment(models.Model):
    """
    Comment Model
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
        )
    name = models.CharField(max_length=80)
    body = models.TextField(max_length=120)
    date_published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date_published"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
