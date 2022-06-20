from django.shortcuts import render, redirect

def home_post(request):
    return render(request, 'main_app/base.html')
