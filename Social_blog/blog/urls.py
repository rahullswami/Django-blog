from django.urls import path
from .views import *


urlpatterns = [
    path('', blog_list , name='blog_list'),
    path('create/new/', create_blog , name='create_blog'),
]