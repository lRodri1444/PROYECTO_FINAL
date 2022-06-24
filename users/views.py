from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .forms import RegisterForm
from main_app.models import user_object

def user_registration(request):    
    if request.method == 'POST':
        registration_form = RegisterForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save()
            user_object.objects.create(
                user = user,
            )
            return redirect('/home/')
    else:
        registration_form = RegisterForm()
    return render(request, 'users/register_template.html', {'registration_form':registration_form})

def LoginView(request):
    return HttpResponseRedirect(reverse('login'))


