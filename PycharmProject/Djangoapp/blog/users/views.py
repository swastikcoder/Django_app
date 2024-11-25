from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login


def home(request):
    return HttpResponse("<h1>This is users page</h1>")
def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request,form.save())
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request,"users/user_register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect('posts')



    else:
        form = AuthenticationForm()
    return render(request,"users/user_login.html", {"form": form})