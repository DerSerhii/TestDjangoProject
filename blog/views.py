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
    # art_python_id = Article.objects.get(title='Python').id
    # art_django_id = Article.objects.get(title='Django').id
    # holovaty_id = UserProfile.objects.get(user__username='Adrian_Holovaty').id
    # rossum_id = UserProfile.objects.get(user__username='Guido_van_Rossum').id
    # willison_id = UserProfile.objects.get(user__username='Simon_Willison').id
    # Comment.objects.bulk_create([
    #     Comment(to_article_id=art_python_id,
    #             author_id=rossum_id,
    #             body="Start comment",
    #             time_create=timezone.now()),
    #     Comment(to_article_id=art_django_id,
    #             author_id=holovaty_id,
    #             body="This comment is in the middle. Will be next",
    #             time_create=timezone.now()),
    #     Comment(to_article_id=art_django_id,
    #             author_id=willison_id,
    #             body="This comment is the last one. Finish",
    #             time_create=timezone.now()),
    # ])
    status['ex_2'] = 'OK'

    # Exercise #3
    # from blog.models import Comment, Article, UserProfile
    # art_python_id = Article.objects.get(title='Python').id
    # rossum_id = UserProfile.objects.get(user__username='Guido_van_Rossum').id
    # com_1 = Comment(to_article_id=art_python_id,
    #                 author_id=rossum_id,
    #                 body="It was a year ago")
    # com_1.save()
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
