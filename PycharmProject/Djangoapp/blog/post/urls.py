from django.urls import path
from . import views
#
urlpatterns = [
    path('', views.post_page),
    path('<slug:slug>',views.post,name = 'post')
]