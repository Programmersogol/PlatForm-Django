from django.urls import path
from .views import PostListView, PostDetailView, PostDeleteView,PostCreateView,UpdatePostView,post_like,add_comment

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<slug:slug>/edit/", UpdatePostView.as_view(), name="post_update"),
    path("post/<slug:slug>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("post/<slug:slug>/", PostDetailView.as_view(), name="post_detail"), 
    path("post/<slug:slug>/like/", post_like, name="post_like"),
    path("post/<slug:slug>/comment/", add_comment, name="add_comment"),


]
