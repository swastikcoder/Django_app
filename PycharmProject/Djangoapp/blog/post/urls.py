from django.urls import path
from . import views
#
urlpatterns = [
    path('', views.post_page,name='posts'),
    path('<slug:slug>',views.post,name = 'post')
]