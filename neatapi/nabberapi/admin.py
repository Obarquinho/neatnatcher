from django.contrib import admin

from .models import Post, User, Country

admin.site.register(Post)
admin.site.register(User)
admin.site.register(Country)

