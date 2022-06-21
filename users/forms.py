from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Widgets

class DateInput(forms.DateInput):
    input_type = 'date'

def placeholder(reference_text):                                   #(string)
    ref = forms.TextInput(attrs={'placeholder':reference_text})
    return ref

# Forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','birth_date','password1','password2']
        widgets = {
            'birth_date':DateInput,
            'email':placeholder('i.e. juansoto1@gmail.com')
        }
