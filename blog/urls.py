"""
urls.py - файл маршрутизатор для Django
"""
from django.contrib import admin
from django.urls import path

from post.views import test_view, hello_view, current_date_view, goodbye_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_view),
    path('hello/', hello_view),
    path('date/', current_date_view),
    path('goodbye/', goodbye_view)
]
