from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('register/', register, name='register'), 
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'), 
    path('profile/', user_profile, name='profile'), 
    path('create/', create, name='create'),
    path('edit/<int:post_id>/', edit, name='edit'),
    path('delete/<int:post_id>/', delete, name='delete'), 
    path('post/<int:post_id>/', post, name='post'), 
    path('tags/<int:tag_id>/', view_tags, name='tag'),
]