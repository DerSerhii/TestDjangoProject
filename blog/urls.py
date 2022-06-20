"This is the urls of the application BLOG"""

from django.urls import path
from .views import view_comments

urlpatterns = [
    path('viewcom', view_comments),
]
