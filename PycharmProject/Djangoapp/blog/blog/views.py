from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,'base.html')

def about(request):
    return render(request,'about.html')