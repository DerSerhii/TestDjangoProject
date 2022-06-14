from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.shortcuts import render
from .models import Comment, Article, LikeDislike

CURRENT_TIME = timezone.now()
CURRENT_DAY = timezone.localdate()


# Exercise #1
def view_comments(request, amount: int = 5, order_reverse: bool = True):
    sign = '-' if order_reverse else ''
    comments = Comment.objects.order_by(f'{sign}time_create')[:amount]
    
    return render(request, 'blog/viewcom.html', {
        'header': 'Latest' if order_reverse else 'First',
        'comments': comments,
    })


# Exercise #2
def create_comments(request):
    Comment.objects.bulk_create([
        Comment(to_article_id="1",
                author_id="2",
                body="Start comment",
                time_create=CURRENT_TIME),
        Comment(to_article_id="2",
                author_id="1",
                body="This comment is in the middle. Will be next",
                time_create=CURRENT_TIME),
        Comment(to_article_id="2",
                author_id="2",
                body="This comment is the last one. Finish",
                time_create=CURRENT_TIME),
    ])
    
    return view_comments(request, 3)


# Exercise #4
def edit_comments(request):
    Comment.objects.filter(body__istartswith='start').update(body='[consored]')
    Comment.objects.filter(body__icontains='middle').update(body='[consored]')
    Comment.objects.filter(body__iendswith='finish').update(body='[consored]')
    
    return view_comments(request, 5)


# Exercise #3
def save_last_year(request):
    a = Comment(to_article_id="1",
                author_id="2",
                body="It was last year!!!")
    a.save_ly()
    
    return view_comments(request, 10, False)


# Exercise #5
def remove_comments(request):
    comments = Comment.objects.filter(body__icontains='k').exclude(body__icontains='c')
    if comments:
        Comment.objects.filter(body__icontains='k').exclude(body__icontains='c').delete()
    
    return render(request, 'blog/viewcom.html', {
        'header': 'Deleted',
        'comments': comments,
    })


# Exercise #6
def comments_article(request):
    comments = Comment.objects.filter(comment__isnull=True).order_by('-author__user__username', 'time_create')[:2]
    return render(request, 'blog/viewcom.html', {
        'header': 'Selective',
        'comments': comments,
    })


# Exercise #7
def various_filters(request):
    first_comment = Comment.objects.earliest('time_create')
    first_comment_of_comment = Comment.objects.filter(comment__isnull=False).earliest('time_create')

    articles = Article.objects.all()
    amount_comments = []
    for article in articles:
        amount_comments.append((article, article.comment_set.count()))

    comm_article_today = Comment.objects.filter(to_article__time_create__gte=CURRENT_DAY)

    good = Comment.objects.filter(body__iexact='Good')
    comm_author = Comment.objects.filter(author__user__username='Adrian_Holovaty')
    comm_without_author = Comment.objects.exclude(author__user__username='Guido_van_Rossum')
    comm_lt = Comment.objects.filter(to_article__id__lt=2)

    return render(request, 'blog/summary.html', {
        'first_comment': first_comment,
        'first_comment_of_comment': first_comment_of_comment,
        'amount_comments': amount_comments,
        'comm_article_today': comm_article_today,
        'good': good,
        'comm_author': comm_author,
        'comm_without_author': comm_without_author,
        'comm_lt': comm_lt,
    })
