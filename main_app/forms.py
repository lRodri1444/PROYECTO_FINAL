from django import forms
from main_app.models import user_object, new_post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewPost(forms.ModelForm):
    class Meta:
        model = new_post
        fields = '__all__'
        exclude = ['user']