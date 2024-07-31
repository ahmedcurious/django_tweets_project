from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tweet(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='registered_users')
    text = models.TextField(max_length=240)
    image = models.ImageField(
        upload_to='tweet_pictures/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.text[:10]}"
