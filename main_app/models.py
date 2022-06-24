import email
from django.db import models
from django.contrib.auth.models import User

class user_object(models.Model):
    user = models.OneToOneField(User, null=True ,on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(default='x152415000kjd52054vdgvd5dscg5026215.png', null=True, blank=True)