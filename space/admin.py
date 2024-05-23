from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'get_image', 'likes')
    list_display_links=('id', 'title')
    
    @admin.display(description='photo')
    def get_image(self, post):
        if post.image:
            return mark_safe(f'<img src="{post.image.url}" width="100px" />')
        return None

admin.site.register(Post, PostAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display=('id', 'first_name', 'last_name', 'username', 'get_image')
    list_display_links=('first_name', 'last_name')

    @admin.display(description='photo')
    def get_image(self, post):
        if post.image:
            return mark_safe(f'<img src="{post.image.url}" width="100px" />')
        return None
    

admin.site.register(UserProfile, UserProfileAdmin)

admin.site.register(Tag)


# Register your models here.
