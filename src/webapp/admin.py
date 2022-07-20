from django.contrib import admin

from .models import Post, Like

class PostAdmin(admin.ModelAdmin):
    pass

class LikeAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)