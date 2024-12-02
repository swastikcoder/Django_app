from django.shortcuts import render,redirect
from .models import Post
from .import forms
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def post_page(request):
    posts = Post.objects.filter(author=request.user)
    return render(request,'post/posts.html', {"posts": posts})

def post(request,slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post/post.html', {'post': post})
@login_required(login_url='/users/login')

def post_new(request):
    if request.method =='POST':
         form = forms.CreatePost(request.POST,request.FILES)
         if form.is_valid():
             new_post = form.save(commit=False)
             new_post.author = request.user
             new_post.save()
             return redirect('posts')

    else:
        form = forms.CreatePost()

    return render(request,'post/new_post.html', {'form': form})
