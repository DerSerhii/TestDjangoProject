from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CandidateCefrForm, AuthenticationBloggerForm, RegistrationBloggerForm, PasswordChangeForm, \
    SearchCommentForm
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


def main(request):
    return render(request, 'blog/index.html')


def blogger_profile(request):
    return render(request, 'blog/profile.html')


def candidate_cefr_form_view(request):
    if request.method == 'POST':
        form = CandidateCefrForm(request.POST)
        if form.is_valid():
            name_candidate = form.cleaned_data['name']
            return render(request, 'blog/cand-cefr-approved.html', {'name': name_candidate})
    else:
        form = CandidateCefrForm()

    return render(request, 'blog/cand-cefr.html', {'form': form})


def blogger_login(request):
    if request.method == 'POST':
        form = AuthenticationBloggerForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return HttpResponseRedirect('/blog')
    else:
        form = AuthenticationBloggerForm()
    
    return render(request, 'blog/login.html', {'form': form})


def blogger_logout(request):
    logout(request)
    return HttpResponseRedirect('/blog/login')


def blogger_register(request):
    if request.method == 'POST':
        form = RegistrationBloggerForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            first_name=form.cleaned_data['first_name'],
                                            last_name=form.cleaned_data['last_name'],
                                            email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/blog')
    else:
        form = RegistrationBloggerForm()

    return render(request, 'blog/registration.html', {'form': form})


@login_required(login_url='/blog/login')
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            request.user.set_password(form.cleaned_data['new_password'])
            request.user.save()
            login(request, request.user)
            return HttpResponseRedirect('/blog')
    else:
        form = PasswordChangeForm()

    return render(request, 'blog/password-change.html', {'form': form})


def search_comment(request):
    form = SearchCommentForm()
    query = None
    results = []
    if request.GET:
        form = SearchCommentForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['search']
            results = Comment.objects.filter(body__icontains=query)
            if 'only_current_user' in request.GET:
                results = results.filter(author__user__username=request.user)

    return render(request, 'blog/search.html', {
        'form': form,
        'query': query,
        'results': results
    })
