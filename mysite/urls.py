"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include, re_path
from myapp.views import main, article_main, articles_archive, users, regex, phone_regex

urlpatterns = [
    path('', main),
    path('articles/', article_main, name='article_main'),
    path('articles/archive', articles_archive, name='article_archive'),
    path('users/', users, name='users_main'),
    path('users/<int:user_number>', users, name='user_number'),
    path('article/', include('myapp.urls')),
    re_path(r'^(?P<text>[\da-f]{4}-\w{6}$)', regex),
    re_path(r'^(?P<number>(067|096|097|098|050|066|095|099|063|073|093)\d{7}$)', phone_regex),
]
