from hashlib import blake2b
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField

class user_object(models.Model):
    user = models.OneToOneField(User, null=True ,on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(default='x152415000kjd52054vdgvd5dscg5026215.png', null=True, blank=True)

class new_post(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = RichTextField(null=True, blank=True)
    posted_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)