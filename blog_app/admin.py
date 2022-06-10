from django.contrib import admin
from .models import UserProfile, PhoneUser, Article, Comments, \
                    CommentsOnComment, LikeDislike

admin.site.register(UserProfile)
admin.site.register(PhoneUser)
admin.site.register(Article)
admin.site.register(Comments)
admin.site.register(CommentsOnComment)
admin.site.register(LikeDislike)
