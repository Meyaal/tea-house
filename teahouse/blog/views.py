from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user_profile.models import UserProfile

from .models import BlogPost, Comment
from .forms import BlogPostForm, CommentForm


def all_posts(request):
    posts = BlogPost.objects.all()

    context = {
        "posts": posts,
    }

    return render(request, "blog/blog.html", context)


@login_required
def add_post(request):
    if not request.user.is_superuser:
        messages.error(
            request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save()
            messages.success(
                request, "Successfully added Post!")
            return redirect(reverse("post_detail", args=[post.id]))
        else:
            messages.error(
                request, "Failed to add post. Please ensure the form is valid."
            )
    else:
        form = BlogPostForm()

    template = "blog/add_post.html"

    context = {"form": form}

    return render(request, template, context)


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user.userprofile
            comment.post = post
            comment.save()
            messages.success(
                request, "Successfully added Comment!")
            return redirect(reverse("post_detail", args=[post.id]))
        else:
            messages.error(
                request, "Failed to add comment. Please ensure the form is valid."
            )
    else:
        form = CommentForm()

    template = "blog/add_comment.html"
    context = {
        "form": form,
        "post": post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    """Delete a Post"""
    if not request.user.is_superuser:
        messages.error(
            request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    post = get_object_or_404(BlogPost, pk=post_id)
    post.delete()
    messages.success(request, "Post deleted!")
    return redirect(reverse("blog"))


@login_required
def delete_comment(request, comment_id):
    """Delete a Comment"""
    post = get_object_or_404(Comment, pk=comment_id)

    if not request.user.is_superuser or not request.user == post.user:
        messages.error(
            request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    post.delete()
    messages.success(request, "Comment deleted!")
    return redirect(reverse("blog"))


@login_required
def edit_post(request, post_id):
    if not request.user.is_superuser:
        messages.error(
            request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    post = get_object_or_404(BlogPost, pk=post_id)

    if request.method == "POST":
        form = BlogPost(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Successfully updated post!")
            return redirect(reverse("post_detail", args=[post.id]))
        else:
            messages.error(
                request, "Failed to update post. Please ensure the form is valid."
            )
    else:
        form = BlogPost(instance=post)
        messages.info(
            request, f"You are editing {post.name}")

    template = "blog/edit_post.html"
    context = {
        "form": form,
        "post": post,
    }

    return render(request, template, context)


@login_required
def edit_comment(request, comment_id):
    post = get_object_or_404(BlogPost, pk=comment_id)

    if not request.user.is_superuser or not post.user == request.user:
        messages.error(
            request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = CommentForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Successfully updated comment!")
            return redirect(reverse("post_detail", args=[post.id]))
        else:
            messages.error(
                request, "Failed to update post. Please ensure the form is valid."
            )
    else:
        form = CommentForm(instance=post)
        messages.info(
            request, f"You are editing {post.name}")

    template = "blog/edit_comment.html"
    context = {
        "form": form,
        "post": post,
    }

    return render(request, template, context)


def post_detail(request, post_id):
    """A view to show individual post"""

    post = get_object_or_404(BlogPost, pk=post_id)
    comments = Comment.objects.filter(
        post=post).order_by("-date")

    context = {"post": post, "comments": comments}

    return render(request, "blog/blog_detail.html", context)
