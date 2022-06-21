from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def my_home(request):
    return render(request, 'main_app/home_template.html')