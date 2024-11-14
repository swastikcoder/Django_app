from django.shortcuts import render
from .models import Post
# Create your views here.

def post_page(request):
    posts = Post.objects.all()
    return render(request,'post/posts.html', {"posts": posts})

