"""
admin.py - для настроек административного сайта
"""

from django.contrib import admin

from post.models import (Post, Products, Comments,
                         Hashtag, Category, Review)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'rate', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'text']


admin.site.register(Products)
admin.site.register(Comments)
admin.site.register(Hashtag)
admin.site.register(Category)
admin.site.register(Review)
