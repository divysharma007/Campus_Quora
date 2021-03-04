from django.contrib import admin

from .models import Post,Enroll,Question,User,category,profile
admin.site.register(Post)
admin.site.register(profile)
admin.site.register(Question)
admin.site.register(Enroll)
admin.site.register(User)
admin.site.register(category)
