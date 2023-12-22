"""
views.py - файл представлений приложений(вьюшек)
"""

from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from post.models import Post, Products, Comments, Hashtag, Category
current_date = date.today()


def main_view(request):
    print(request.method)
    if request.method == 'GET':
        return render(request, 'index.html')


def current_date_view(request):
    if request.method == 'GET':
        return HttpResponse(current_date)


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse('BYE BYE!!!!!!!')


def post_list_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'post/list.html', context=context)


def hashtag_list_view(reqeust):
    if reqeust.method == 'GET':
        hashtags = Hashtag.objects.all()

    context = {
        'hashtags' : hashtags
    }
    return render(
        reqeust,
        'hashtag/list.html',
        context=context
    )


def products_view(request):
    if request.method == 'GET':
        products = Products.objects.all()
        context = {
            'products': products
        }
        return render(request, 'product/products.html', context=context)


def category_list_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'category/category.html', context=context)

# Create your views here.
