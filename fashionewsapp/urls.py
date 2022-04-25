from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_post/', views.CreatePost.as_view(), name='add_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('edit_post/<slug>/', views.EditPost.as_view(), name='edit_post'),
    path('delete_post/<slug>/', views.DeletePost.as_view(), name='delete_post')

]
