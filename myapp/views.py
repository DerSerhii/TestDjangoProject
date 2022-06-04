"""This is the CONTROLLER"""

from django.http import HttpResponse


def main(request):
    """accepts a request and returns a response with text"""
    return HttpResponse("Homepage")


def article_main(request):
    """accepts a request and returns a response with text"""
    return HttpResponse('This is the main page of articles')


def articles_archive(request):
    """accepts a request and returns a response with text"""
    return HttpResponse('This is the page with archived articles')


def users(request, user_number=''):
    """accepts a request and returns a response with text"""
    text = f"user #{user_number}" if user_number else "all users"
    return HttpResponse(f"This is the page of {text}")


def article(request, article_number, slug_text=''):
    """accepts a request and returns a response with text with the parameter in url"""
    return HttpResponse(
        "This is an article #{}. {}".format(
            article_number, "Name of this article is {}".format(
                slug_text) if slug_text else "This is unnamed article"))


def article_archive(request, article_number):
    """accepts the request and returns a response with the text with the parameter in url"""
    return HttpResponse(f"This is an archive of article #{article_number}!")


def regex(request, text):
    """accepts the request and returns a response with the text with the parameter in url"""
    return HttpResponse(f"it's regexp with text: {text}")


def phone_regex(request, number):
    """accepts the request and returns a response with the text with the parameter in url"""
    return HttpResponse(f"This page of Ukrainian phone number: +38{number}")
