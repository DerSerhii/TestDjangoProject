"""That's the CONTROLLER"""

from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    """
    Combines a given template with a given context dictionary
    and returns an HttpResponse object with that rendered text
    """

    return render(request, 'myapp/index.html')


def article_main(request):
    """
    Combines a given template with a given context dictionary
    and returns an HttpResponse object with that rendered text
    """

    return render(request, 'myapp/page.html', {'header': 'Articles'})


def articles_archive(request):
    """
    Combines a given template with a given context dictionary
    and returns an HttpResponse object with that rendered text
    """

    return render(request, 'myapp/page.html', {'header': 'Article archive'})


def users(request, user_number=''):
    """
    Combines a given template with a given context dictionary
    and returns an HttpResponse object with that rendered text
    """

    header = f"User #{user_number}" if user_number else "All site users"
    return render(request, 'myapp/page.html', {'header':  header})


def article(request, article_number, slug_text=''):
    """
    Combines a given template with a given context dictionary
    and returns an HttpResponse object with that rendered text
    """

    header = f"Article #{article_number}"
    return render(request, 'myapp/article.html', {
        'header':  header,
        'article_number': article_number,
        'slug': slug_text,
    })


def article_archive(request, article_number):
    """
    Combines a given template with a given context dictionary
    and returns an HttpResponse object with that rendered text
    """

    header = f"Article archive #{article_number}"
    return render(request, 'myapp/page.html', {'header':  header})


def regex(request, text):
    """accepts the request and returns a response with the text with the parameter in url"""
    return HttpResponse(f"it's regexp with text: {text}")


def phone_regex(request, number):
    """accepts the request and returns a response with the text with the parameter in url"""
    return HttpResponse(f"This page of Ukrainian phone number: +38{number}")
