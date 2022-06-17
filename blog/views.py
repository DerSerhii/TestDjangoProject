from django.shortcuts import render
from .models import Comment


def view_comments(request):
    status = dict()

    # Exercise #1
    comments = Comment.objects.order_by('-time_create')[:5]
    status['ex_1'] = 'OK'

    # Exercise #2
    # from blog.models import Comment, Article, UserProfile
    # from django.contrib.auth.models import User
    # from django.utils import timezone
    # user1 = User.objects.create(username="user1")
    # user2 = User.objects.create(username="user2")
    # user_prof_1 = UserProfile.objects.create(user=user1)
    # user_prof_2 = UserProfile.objects.create(user=user2)
    # article_1 = Article.objects.create(title="Article 1",content="something",author=user_prof_1,time_create=timezone.now())
    # article_2 = Article.objects.create(title="Article 2",content="something",author=user_prof_1,time_create=timezone.now())
    # Comment.objects.bulk_create([
    #     Comment(to_article=article_1,
    #             author=user_prof_1,
    #             body="Start comment",
    #             time_create=timezone.now()),
    #     Comment(to_article=article_2,
    #             author=user_prof_2,
    #             body="This comment is in the middle. Will be next",
    #             time_create=timezone.now()),
    #     Comment(to_article=article_1,
    #             author=user_prof_2,
    #             body="This comment is the last one. Finish",
    #             time_create=timezone.now()),
    # ])
    status['ex_2'] = 'OK'

    # Exercise #3
    # from blog.models import Comment, Article, UserProfile
    # from django.contrib.auth.models import User
    # from django.utils import timezone
    # user3 = User.objects.create(username="user3")
    # user_prof_3 = UserProfile.objects.create(user=user3)
    # article_3 = Article.objects.create(title="Article 3",content="something",author=user_prof_3,time_create=timezone.now())
    # com = Comment(to_article=article_3,
    #               author=user_prof_3,
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
