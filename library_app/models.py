from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


class UserProf(models.Model):
    user_prof = models.OneToOneField(User, on_delete=models.CASCADE)
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
    user = models.ForeignKey(UserProf, on_delete=models.CASCADE, related_name='phone_user')

    def __str__(self):
        return self.phone


class Author(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    kind_genre = models.CharField(max_length=20)

    def __str__(self):
        return self.kind_genre


class Book(models.Model):
    book_title = models.CharField(max_length=20)
    book_author = models.ManyToManyField(Author)
    book_genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genre')
    book_year_public = models.DateField(null=True, blank=True)
    book_available = models.BooleanField(default=True)

    def __str__(self):
        return self.book_title


class UseBook(models.Model):
    user_book = models.ForeignKey(UserProf, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    date_of_taking = models.DateField()
    return_date = models.DateField(null=True)

    def __str__(self):
        return self.user_book, self.book
