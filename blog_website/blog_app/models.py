from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    nick_name = models.CharField(max_length=200, blank=True)
    sex = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


class Newpost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    post_name = models.CharField(max_length=100)
    post = models.CharField(max_length=1000)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post_name + ' (' + self.author.username + ')'
