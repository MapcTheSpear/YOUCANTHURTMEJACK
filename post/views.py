"""
views.py - файл представлений приложений(вьюшек)
"""

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from post.forms import PostForm, ProductForm, CategoryForm, ReviewForm
from datetime import date
from post.models import Post, Products, Comments, Hashtag, Category, Review
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


def post_detail_view(request, post_id):
    if request.method == "GET":
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return HttpResponse('404 not found')

        context = {
            'post': post
        }
        return render(
            request,
            'post/detail.html',
            context=context
        )


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


def product_detail_view(request, product_id):
    if request.method == 'GET':
        try:
            product = Products.objects.get(id=product_id)
            form = ReviewForm(request.method)
        except Products.DoesNotExist:
            return HttpResponse('404 not found')

        context = {
            'product': product,
            'form': ReviewForm
        }
        return render(
            request,
            'product/detail.html',
            context=context
        )
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        product = Products.objects.get(id=product_id)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = product
            form.save()
            return redirect('.')
        else:
            context = {
                'form': form
            }
            return render(request, 'product/detail.html', context=context)



def category_list_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'category/category.html', context=context)


def post_create_view(request):
    if request.method == 'GET':
        context = {
            'form': PostForm,
        }
        return render(request, 'post/create.html', context=context)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            return redirect('/posts/')
        context = {
            'form': form,
        }

        return render(request, 'post/create.html', context=context)


def create_product_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductForm,
        }
        return render(request, 'product/create.html', context=context)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            Products.objects.create(**form.cleaned_data)
            return redirect('/products/')
        context = {
            'form': form,
        }

        return render(request, 'product/create.html', context=context)


def create_category_view(request):
    if request.method == 'GET':
        context = {
            'form': CategoryForm,
        }
        return render(request, 'category/create.html', context=context)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect('/products/')
        context = {
            'form': form,
        }

        return render(request, 'category/create.html', context=context)



# Create your views here.

