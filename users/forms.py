from django import forms
from main_app.models import user_object
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Widgets

class DateInput(forms.DateInput):
    input_type = 'date'

def placeholder(reference_text):                                   #(string)
    ref = forms.TextInput(attrs={'placeholder':reference_text})
    return ref

def form_field_size():                                             #()
    size = forms.TextInput(attrs={'class':'narrow-select'})
    return size



# Forms

class UserObjectForm(forms.ModelForm):
    class Meta:
        model = user_object
        fields = '__all__'
        exclude = ['user',]

class RegisterForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'pass', 'type':'password', 'align':'center'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'pass', 'type':'password', 'align':'center'}),
    )

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username':form_field_size(),
            'email':form_field_size(),
        }
