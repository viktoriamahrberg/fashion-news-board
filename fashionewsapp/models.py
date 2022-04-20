from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Post Model
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="news_post")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='news_image')
    excerpt = models.TextField(blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
    original_news_link = models.URLField(blank=False)

    class Meta:
        ordering = ['date_published']

    def __str__(self):
        return self.title

    def get_cat_list(self):
        k = self.category # for now ignore this instance method
        
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]


class Comment(models.Model):
    """
    Comment Model
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    body = models.TextField(max_length=120)
    date_published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date_published"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


