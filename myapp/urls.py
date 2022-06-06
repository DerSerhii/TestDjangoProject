"""This is the urls of the application MYAPP"""

from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', main, name='home'),
    path('articles/', article_main, name='article_main'),
    path('articles/archive', articles_archive, name='article_archive'),
    path('users/', users, name='users_main'),
    path('users/<int:user_number>', users, name='user_number'),
    path('article/<int:article_number>/', article, name='article'),
    path('article/<int:article_number>/archive', article_archive, name='article_archive'),
    path('article/<int:article_number>/<slug:slug_text>', article, name='article'),
    re_path(r'^(?P<text>[\da-f]{4}-\w{6}$)', regex),
    re_path(r'^(?P<number>(067|096|097|098|050|066|095|099|063|073|093)\d{7}$)', phone_regex),
]
