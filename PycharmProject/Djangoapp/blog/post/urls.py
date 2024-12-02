from django.urls import path
from . import views
#
urlpatterns = [
    path('', views.post_page,name='posts'),
    path('new_post/',views.post_new,name ='new-post'),
    path('<slug:slug>',views.post,name = 'post')
]