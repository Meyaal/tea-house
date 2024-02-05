from django.db import models
from user_profile.models import UserProfile
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length=512)
    content = models.TextField()
    user = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True
    )
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])


# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True
    )
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        BlogPost, on_delete=models.SET_NULL, null=True, blank=True)
