"This is the urls of the application BLOG"""

from django.urls import path
from .views import view_comments, create_comments, edit_comments, save_last_year, \
    remove_comments, comments_article, various_filters

urlpatterns = [
    path('viewcom', view_comments),
    path('createcom', create_comments),
    path('editcom', edit_comments),
    path('savecom', save_last_year),
    path('removecom', remove_comments),
    path('articlecom', comments_article),
    path('summary', various_filters),
]
