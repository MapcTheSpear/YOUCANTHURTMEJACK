"""
admin.py - для настроек административного сайта
"""

from django.contrib import admin
from post.models import Post, Products


admin.site.register(Post)
admin.site.register(Products)
