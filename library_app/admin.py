from django.contrib import admin
from .models import UserProf, PhoneUser, Author, Genre, Book, UseBook


admin.site.register(UserProf)
admin.site.register(PhoneUser)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(UseBook)
