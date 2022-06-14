from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class UserProfile(models.Model):
    message = 'Phone number must be entered in the format: 06751102' \
              'sd00'

    regex = RegexValidator(
        regex=r'^(067|096|097|098|050|066|095|099|063|073|093)\d{7}$',
        message=message)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True, upload_to='photo_users')
    phone = models.CharField(null=True, blank=True, validators=[regex], max_length=10, unique=True)
    info = models.CharField(null=True, blank=True, max_length=255)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.user.username


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=False)
    time_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    like = GenericRelation('LikeDislike')

    class Meta:
        ordering = ['-time_create']

    def __str__(self):
        return self.title


class Comment(models.Model):
    to_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    body = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=False)
    time_update = models.DateTimeField(auto_now=True)
    comment = models.ForeignKey('blog.Comment', null=True, blank=True, on_delete=models.CASCADE,
                                related_name='comments')
    active = models.BooleanField(default=True)
    like = GenericRelation('LikeDislike')

    class Meta:
        ordering = ['-time_create']

    def save_ly(self, **kwargs):
        if not self.id:
            current = timezone.now()
            if current.month == 2 and current.day == 29:
                last_year = current.replace(year=current.year - 1, day=28)
            else:
                last_year = current.replace(year=current.year - 1)
            # or install PyPI relativedelta
            self.time_create = last_year
        super().save(**kwargs)

    def __str__(self):
        return self.body[:50]


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = 0

    VOTES = (
        (DISLIKE, _('Dislake')),
        (LIKE, _('Like'))
    )

    vote = models.SmallIntegerField(choices=VOTES, default=LIKE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.VOTES[self.vote][1]
