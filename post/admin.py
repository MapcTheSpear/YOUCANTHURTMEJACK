"""
admin.py - для настроек административного сайта
"""

from django.contrib import admin
from post.models import (Post, Products, Comments,
                         Hashtag)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'rate', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    readonly_fields = ['title']
    search_fields = ['title', 'text']


admin.site.register(Products)
admin.site.register(Comments)
admin.site.register(Hashtag)
