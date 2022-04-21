from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Comment
from .forms import CommentForm, AddPostForm
from django.views.generic.edit import CreateView



class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by("-date_published")
    template_name = 'index.html'
    paginate_by = 4


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.order_by('date_published')
        # liked = False
        # if post.likes.filter(id=self.request.user.id).exists()
        return render (
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

        return render (
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
   
        model = Post
        form_class = AddPostForm
        template_name = 'add_post.html'

   

    #     add_post_form = AddPostForm(data=request.POST)
    #     if add_post_form.is_valid():
    #         add_post_form.instance.email = request.user.email
    #         add_post_form.instance.name = request.user.username
    #         add_post = add_post_form.save(commit=False)
    #         add_post.post = post
    #         add_post.save()
    #     else:
    #         add_post_form = AddPostForm()

    #     return render (
    #         request,
    #         "add_post.html",
    #         {
    #             "add_post_form": AddPostForm(),
    #         }
    #     )