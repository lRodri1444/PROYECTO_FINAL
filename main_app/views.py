from cmath import e
from .models import user_object, new_post
from .forms import NewPost
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from users.forms import RegisterForm, UserObjectForm
from django.http import Http404

@login_required
def my_home(request):
    posts = new_post.objects.all().order_by('-posted_date')
    post = NewPost()
    if request.method == 'POST':
        post = NewPost(request.POST)
        if post.is_valid():
            obj = post.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, 'Your post was submitted')
    context = {
        'NewPost':post,
        'posts':posts
    }
    return render(request, 'main_app/home_template.html',context)

@login_required
def users_profile(request):
    posts = new_post.objects.all()
    posts = posts.filter(user=request.user).order_by('-posted_date')
    context = {
        'posts':posts
    }
    return render(request, 'main_app/profile_template.html', context)

@login_required
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

@login_required
def extra_update_profile(request):
    extra_user_inst = request.user.user_object
    extra_edit_form = UserObjectForm(request.POST or None, instance=extra_user_inst)

    if request.method == 'POST':
        extra_edit_form = UserObjectForm(request.POST, request.FILES,instance=extra_user_inst)  
        if extra_edit_form.is_valid():
            extra_edit_form.save()
            messages.info(request, 'Profile updated')
            return redirect('/home/profile/')
    context = {
        'extra_edit_form':extra_edit_form
    }
    return render(request, 'main_app/extra_edit_data.html', context)

@login_required
def pages(request, post_id):
    posts = new_post.objects.all()
    posts = posts.get(id=post_id)
    context = {
        'posts':posts
    }
    return render(request, 'main_app/blog_pages.html', context)
    
@login_required
def update_page(request, post_id):
    posts = new_post.objects.all()
    posts = posts.get(id=post_id)

    if request.user.is_superuser or posts.user.id == request.user.id:
        post_form = NewPost(instance=posts)

        if request.method == 'POST':
            post_form = NewPost(request.POST, instance=posts)
            if post_form.is_valid():
                post_form.save()
                messages.info(request, 'Post updated')
                return redirect('/home/profile/')
    else:
        return redirect('/home/profile/')
    context = {
        'posts':posts,
        'post_form':post_form
    }
    return render(request, 'main_app/update_pages.html', context)

@login_required
def delete_page(request, post_id):
    post_to_delete = new_post.objects.all()
    post_to_delete = post_to_delete.get(id=post_id)
    try:
        if post_to_delete.user.id == request.user.id or request.user.is_superuser:
            post_to_delete.delete()
            messages.info(request, 'Post deleted')
    except:
        raise Http404() 

    return redirect('/home/profile/')

@login_required
def profiles_list(request, profile_id):
    profile_owner = User.objects.get(id = profile_id)
    profile_posts = new_post.objects.filter(user_id = profile_owner.id).order_by('-posted_date')

    if profile_owner.id == request.user.id:
        return redirect('/home/profile/')

    context = {
        'profile_owner':profile_owner,
        'posts':profile_posts
    }
    return render(request, 'main_app/public_profile.html', context)


@staff_member_required
def posts_control(request):
    posts = new_post.objects.all()

    return render(request, 'main_app/posts_RUD.html', {'posts':posts})
