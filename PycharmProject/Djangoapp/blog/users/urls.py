from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='user'),
    path('register/',views.user_register,name = "register"),
    path('login/',views.login_view, name = "login"),
    path('logout/', views.logout_view, name="logout")

]