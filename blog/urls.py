"""
urls.py - файл маршрутизатор для Django
"""
from django.contrib import admin
from django.urls import path
from django.urls import reverse
from django.conf.urls.static import static
from django.conf import settings

from post.views import (main_view, current_date_view, goodbye_view,
                        post_list_view, products_view, hashtag_list_view,
                        category_list_view, post_detail_view, product_detail_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('date/', current_date_view),
    path('goodbye/', goodbye_view),
    path('posts/', post_list_view),
    path('products/', products_view),
    path('hashtags/', hashtag_list_view),
    path('category/', category_list_view),
    path('posts/<int:post_id>/', post_detail_view),
    path('products/<int:product_id>/', product_detail_view)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
