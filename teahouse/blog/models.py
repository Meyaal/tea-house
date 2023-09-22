from django.db import models
from user_profile.models import UserProfile


class BlogPost(models.Model):
    title = models.CharField(max_length=512)
    content = models.TextField()
    user = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True
    )
    date = models.DateTimeField(auto_now_add=True)


# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True
    )
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        BlogPost, on_delete=models.SET_NULL, null=True, blank=True
    )
