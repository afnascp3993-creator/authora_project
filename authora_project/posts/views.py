from django.shortcuts import render, redirect, get_object_or_404
from .models import Posts
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



def post_list(request):
    posts = Posts.objects.all()
    return render(request,'posts/post_list.html',{'posts':posts})

def user_post_list(request):
     posts = Posts.objects.filter(status='approved')
     return render(request,'posts/user_post_list.html',{'posts':posts})


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post =form.save(commit=False)
            post.status='pending'
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect('user_post_list')

    else:
        form = PostForm()
    return render(request,'posts/post_form.html',{'form':form})


def post_update(request,id):
    post = get_object_or_404(Posts,id=id)

    if request.method == "POST":
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            messages.info(request,"Post updated successfully")
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
        messages.error(request,"Something went wrong")
    return render(request,'posts/post_form.html',{'form':form})


def post_delete(request,id):
    post = get_object_or_404(Posts,id=id)

    if request.method == "POST":
        post.delete()
        messages.warning(request,"Post deleted successfully")
        return redirect('post_list')

    return render(request,'posts/post_delete.html',{'post':post})



def post_detail(request, id):

    post = get_object_or_404(Posts, id=id)

    # Next post
    next_post = Posts.objects.filter(id__gt=id).order_by('id').first()

    # Previous post
    prev_post = Posts.objects.filter(id__lt=id).order_by('-id').first()

    # Related posts (same category)
    related_posts = Posts.objects.filter(category=post.category).exclude(id=id)[:3]

    context = {
        'post': post,
        'next_post': next_post,
        'prev_post': prev_post,
        'related_posts': related_posts
    }

    return render(request, 'posts/post_detail.html', context)

def admin_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post_list')
        else:
            messages.error(request,"Invalid username or password")
    return render(request,'login.html')

def admin_logout(request):

    request.session.flush()

    return redirect('login')


def user_post_detail(request, id):
    post = get_object_or_404(Posts, id=id, status='approved')

    # Next approved post
    next_post = Posts.objects.filter(id__gt=id, status='approved').order_by('id').first()

    # Previous approved post
    prev_post = Posts.objects.filter(id__lt=id, status='approved').order_by('-id').first()

    # Related approved posts (same category)
    related_posts = Posts.objects.filter(category=post.category, status='approved').exclude(id=id)[:3]

    context = {
        'post': post,
        'next_post': next_post,
        'prev_post': prev_post,
        'related_posts': related_posts
    }

    return render(request, 'posts/user_post_detail.html', context)

