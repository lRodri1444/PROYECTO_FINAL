from django import forms
from main_app.models import user_object, new_post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Widgets

def form_field_size():                                             #()
    size = forms.TextInput(attrs={'class':'narrow-select'})
    return size

class NewPost(forms.ModelForm):
    class Meta:
        model = new_post
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'title':form_field_size()
        }