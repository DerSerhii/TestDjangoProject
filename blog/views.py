from django.shortcuts import render
from .models import Comment


def view_comments(request):
    status = dict()

    # Exercise #1
    comments = Comment.objects.order_by('-time_create')[:5]
    status['ex_1'] = 'OK'

    # Exercise #2
    # from blog.models import Comment
    # from django.utils import timezone
    # Comment.objects.bulk_create([
    #     Comment(to_article_id="1",
    #             author_id="2",
    #             body="Start comment",
    #             time_create=timezone.now()),
    #     Comment(to_article_id="2",
    #             author_id="1",
    #             body="This comment is in the middle. Will be next",
    #             time_create=timezone.now()),
    #     Comment(to_article_id="2",
    #             author_id="2",
    #             body="This comment is the last one. Finish",
    #             time_create=timezone.now()),
    # ])
    status['ex_2'] = 'OK'

    # Exercise #3
    # from blog.models import Comment
    # a = Comment(to_article_id="1",
    #             author_id="2",
    #             body="It was a year ago")
    # a.save()
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
