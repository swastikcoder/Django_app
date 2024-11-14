from django.shortcuts import render
from .models import Post
# Create your views here.
from django.http import HttpResponse

def post_page(request):
    posts = Post.objects.all()
    return render(request,'post/posts.html', {"posts": posts})

def post(request,slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post/post.html', {'post': post})



