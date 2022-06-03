"""This is the urls of the application MYAPP"""

from django.urls import path
from .views import article, article_archive

urlpatterns = [
    path('<int:article_number>/', article, name='article'),
    path('<int:article_number>/archive', article_archive, name='article_archive'),
    path('<int:article_number>/<slug:slug_text>', article, name='article'),
]
