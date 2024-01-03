from django.urls import path

from post import views


urlpatterns = [
    path('', views.main_view),
    path('home/', views.main_view),
    path('date/', views.current_date_view),
    path('goodbye/', views.goodbye_view),
    path('posts/', views.post_list_view),
    path('products/', views.products_view),
    path('hashtags/', views.hashtag_list_view),
    path('category/', views.category_list_view),
    path('posts/create/', views.post_create_view),
    path('posts/<int:post_id>/', views.post_detail_view),
    path('products/create/', views.create_product_view),
    path('products/<int:product_id>/', views.product_detail_view),
    path('category/create/', views.create_category_view),
]