from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.validators import RegexValidator
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20)
    user_photo = models.ImageField(upload_to='photo_users', verbose_name='Photo', null=True)

    user_url = models.URLField()
    user_info = models.CharField(max_length=255, default='Information is absent')

    def __str__(self):
        return self.user_name


class PhoneUser(models.Model):
    phone_message = 'Phone number must be entered in the format: 0675110200'

    phone_regex = RegexValidator(
        regex=r'^(067|096|097|098|050|066|095|099|063|073|093)\d{7}$',
        message=phone_message)

    phone = models.CharField(validators=[phone_regex], max_length=10,
                             null=True, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='phone')

    def __str__(self):
        return self.phone


class Article(models.Model):
    article_title = models.CharField(max_length=100, verbose_name="Title")
    article_content = models.TextField(blank=True, verbose_name="Content")
    article_time_create = models.DateTimeField(auto_now_add=True)
    article_time_update = models.DateTimeField(auto_now=True)
    article_author_id = models.ForeignKey(UserProfile,
                                          on_delete=models.CASCADE,
                                          related_name='author')
    article_like = GenericRelation('LikeDislike', related_query_name='articles')

    def __str__(self):
        return self.article_title


class Comments(models.Model):
    comment_article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_author_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment_time_create = models.DateTimeField(auto_now_add=True)
    comment_time_update = models.DateTimeField(auto_now=True)
    comment_body = models.CharField(max_length=255)
    comment_active = models.BooleanField(default=True)
    comment_like = GenericRelation('LikeDislike', related_query_name='comments')

    def __str__(self):
        return self.comment_body[:10]


class CommentsOnComment(models.Model):
    coc_comment_id = models.ForeignKey(Comments, on_delete=models.CASCADE)
    coc_author_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    coc_time_create = models.DateTimeField(auto_now_add=True)
    coc_time_update = models.DateTimeField(auto_now=True)
    coc_body = models.CharField(max_length=255)
    coc_active = models.BooleanField(default=True)
    coc_like = GenericRelation('LikeDislike', related_query_name='comments_on_comment')

    def __str__(self):
        return self.coc_body[:10]


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, 'Dislake'),
        (LIKE, 'Like')
    )

    vote = models.SmallIntegerField(choices=VOTES, default=LIKE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    like_time_create = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.vote
