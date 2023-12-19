"""
urls.py - файл маршрутизатор для Django
"""
from django.contrib import admin
from django.urls import path
from django.urls import reverse

from post.views import main_view, current_date_view, goodbye_view, post_list_view, products_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('date/', current_date_view),
    path('goodbye/', goodbye_view),
    path('posts/', post_list_view),
    path('products/', products_view)
]
