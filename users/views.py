from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .forms import RegisterForm

def user_registration(request):    
    if request.method == 'POST':
        registration_form = RegisterForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
    else:
        registration_form = RegisterForm()
    return render(request, 'users/register_template.html', {'registration_form':registration_form})

def LoginView(request):
    return HttpResponseRedirect(reverse('login'))
