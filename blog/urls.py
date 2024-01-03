"""
urls.py - файл маршрутизатор для Django
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import reverse
from django.conf.urls.static import static
from django.conf import settings

from post.views import (main_view, current_date_view, goodbye_view,
                        post_list_view, products_view, hashtag_list_view,
                        category_list_view, post_detail_view, product_detail_view,
                        post_create_view, create_product_view, create_category_view,
                        )
from user.views import (register_view, login_view, logout_view,
                        profile_view, delete_profile_view,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('', include('post.urls')),
    path('auth/', include('user.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
