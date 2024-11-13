from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Post

def posts(request):
    posts = Post.objects.all().order_by('date')
    return render(request,'post/post_da.html', {'posts':posts})
