from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.validators import RegexValidator
from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photo_users', verbose_name='Photo', null=True)

    url = models.URLField()
    info = models.CharField(max_length=255, default='Information is absent')

    def __str__(self):
        return self.name


class PhoneUser(models.Model):
    message = 'Phone number must be entered in the format: 0675110200'

    regex = RegexValidator(
        regex=r'^(067|096|097|098|050|066|095|099|063|073|093)\d{7}$',
        message=message)

    phone = models.CharField(validators=[regex], max_length=10,
                             null=True, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.phone


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    content = models.TextField(blank=True, verbose_name="Content")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    like = GenericRelation('LikeDislike')

    def __str__(self):
        return self.title


class Comments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    body = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    like = GenericRelation('LikeDislike')

    def __str__(self):
        return self.body[:10]


class CommentsOnComment(models.Model):
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    body = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    like = GenericRelation('LikeDislike')

    def __str__(self):
        return self.body[:10]


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, 'Dislake'),
        (LIKE, 'Like')
    )

    vote = models.SmallIntegerField(choices=VOTES, default=LIKE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.vote
