from django.shortcuts import render
from .models import Comment


def view_comments(request):
    status = dict()

    # Exercise #1
    comments = Comment.objects.order_by('-time_create')[:5]
    status['ex_1'] = 'OK'

    # Exercise #2
    # from blog.models import Comment, Article, UserProfile
    # from django.utils import timezone
    # article_1 = Article.objects.get(pk=1)
    # article_2 = Article.objects.get(pk=2)
    # author_1 = UserProfile.objects.get(pk=1)
    # author_2 = UserProfile.objects.get(pk=2)
    # author_3 = UserProfile.objects.get(pk=3)
    # Comment.objects.bulk_create([
    #     Comment(to_article=article_1,
    #             author=author_1,
    #             body="Start comment",
    #             time_create=timezone.now()),
    #     Comment(to_article=article_2,
    #             author=author_2,
    #             body="This comment is in the middle. Will be next",
    #             time_create=timezone.now()),
    #     Comment(to_article=article_1,
    #             author=author_3,
    #             body="This comment is the last one. Finish",
    #             time_create=timezone.now()),
    # ])
    status['ex_2'] = 'OK'

    # Exercise #3
    # from blog.models import Comment, Article, UserProfile
    # article = Article.objects.get(pk=1)
    # author = UserProfile.objects.get(pk=2)
    # com = Comment(to_article=article,
    #               author=author,
    #               body="It was a year ago !!!")
    # com.save()
    status['ex_3'] = 'OK'

    # Exercise #4
    # from blog.models import Comment
    # Comment.objects.filter(body__istartswith='start').update(body='[consored]')
    # Comment.objects.filter(body__icontains='middle').update(body='[consored]')
    # Comment.objects.filter(body__iendswith='finish').update(body='[consored]')
    status['ex_4'] = 'OK'

    # Exercise #5
    # from blog.models import Comment
    # comments = Comment.objects.filter(body__icontains='k').exclude(body__icontains='c').delete()
    status['ex_5'] = 'OK'

    # Exercise #6
    # from blog.models import Comment
    # find = Comment.objects.filter(comment__isnull=True).order_by('-author__user__username', 'time_create')[:2]
    status['ex_6'] = 'OK'

    return render(request, 'blog/viewcom.html', {
        'header': 'Сomments',
        'comments': comments,
        'status': status,
    })
