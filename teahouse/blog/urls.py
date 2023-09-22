from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_posts, name="blog"),  # List all posts
    path("add/", views.add_post, name="add_post"),  # Add a new post
    path(
        "<int:post_id>/add_comment/", views.add_comment, name="add_comment"
    ),  # Add a new comment
    path(
        "<int:post_id>/", views.post_detail, name="post_detail"
    ),  # Detail view for a specific post
    path(
        "edit/<int:post_id>/", views.edit_post, name="edit_post"
    ),  # Edit a specific post
    path(
        "edit_comment/<int:comment_id>/", views.edit_comment, name="edit_comment"
    ),  # Edit a specific comment
    path(
        "delete/<int:post_id>/", views.delete_post, name="delete_post"
    ),  # Delete a specific post
    path(
        "delete_comment/<int:comment_id>/", views.delete_comment, name="delete_comment"
    ),  # Delete a specific comment
]
