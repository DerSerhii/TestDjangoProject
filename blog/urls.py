"This is the urls of the application BLOG"""

from django.urls import path
from .views import main, view_comments, candidate_cefr_form_view,\
    blogger_login, blogger_logout, blogger_register, \
    password_change, blogger_profile, search_comment

urlpatterns = [
    path('', main, name='home'),
    path('register/', blogger_register, name='register'),
    path('login/', blogger_login, name='login'),
    path('logout/', blogger_logout, name='logout'),
    path('profile/', blogger_profile, name='profile'),
    path('password-change/', password_change, name='password-change'),
    path('cand-cefr/', candidate_cefr_form_view, name='cand-cefr-form'),
    path('search-comment/', search_comment, name='search-comment'),
    path('viewcom/', view_comments),
]
