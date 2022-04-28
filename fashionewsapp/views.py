from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.urls import reverse_lazy
from .models import Post
from .forms import CommentForm, AddPostForm, EditPostForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class PostList(generic.ListView):
    """
    View for displaying posts list on index.html
    """
    model = Post
    queryset = Post.objects.order_by("-date_published")
    template_name = 'index.html'
    paginate_by = 4


class PostDetail(View):
    """
    View for displaying posts individually
    """
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.order_by('date_published')

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": CommentForm(),
            }
        )

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.order_by('date_published')

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": CommentForm(),
            }
        )


class CreatePost(CreateView):
    """
    View for creating posts on add_post.html
    """
    model = Post
    form_class = AddPostForm
    template_name = 'add_post.html'


class EditPost(UpdateView):
    """
    View for editing posts on edit_post.html
    """
    model = Post
    form_class = EditPostForm
    template_name = 'edit_post.html'


class DeletePost(DeleteView):
    """
    View for deleting post
    """
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


