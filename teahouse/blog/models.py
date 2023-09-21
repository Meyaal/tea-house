from django.db import models

from user_profile.models import UserProfile


# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True
    )
    date = models.DateTimeField(auto_now_add=True)
    replys = models.ForeignKey(
        Comment, on_delete=models.SET_NULL, null=True, blank=True
    )


class BlogPost(models.Model):
    title = models.CharField(max_length=512)
    content = models.TextField()
    user = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True
    )
    date = models.DateTimeField(auto_now_add=True)
    replys = models.ForeignKey(
        Comment, on_delete=models.SET_NULL, null=True, blank=True
    )
