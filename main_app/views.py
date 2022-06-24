from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from users.forms import RegisterForm, UserObjectForm

@login_required
def my_home(request):
    return render(request, 'main_app/home_template.html')

def users_profile(request):
    return render(request, 'main_app/profile_template.html')

def update_profile(request):
    user_inst = request.user
    edit_form = RegisterForm(instance=user_inst)
    
    if request.method == 'POST':
        edit_form = RegisterForm(request.POST, instance=user_inst)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('/login/')
    context = {
        'edit_form':edit_form,
    }
    return render(request, 'main_app/edit_data.html', context)

def extra_update_profile(request):
    extra_user_inst = request.user.user_object
    extra_edit_form = UserObjectForm(request.POST or None, instance=extra_user_inst)

    if request.method == 'POST':
        extra_edit_form = UserObjectForm(request.POST, request.FILES,instance=extra_user_inst)  
        if extra_edit_form.is_valid():
            extra_edit_form.save()
            return redirect('/home/profile/')
    context = {
        'extra_edit_form':extra_edit_form
    }
    return render(request, 'main_app/extra_edit_data.html', context)