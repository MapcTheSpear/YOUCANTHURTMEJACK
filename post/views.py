"""
views.py - файл представлений приложений(вьюшек)
"""

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db.models import Q
from django.conf import settings
from post.forms import PostForm, ProductForm, CategoryForm, ReviewForm, PostForm2, ProductForm2
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
        search = request.GET.get('search')
        order = request.GET.get('order')
        if search:
            posts = posts.filter(
                Q(title__icontains=search) | Q(text__icontains=search)
            )
            # posts = posts.filter(title__contains=search) | posts.filter(text__icontains=search)
        if order == 'date':
            posts = posts.order_by('created_at')
        if order == '-date':
            posts = posts.order_by('-created_at')
        if order == 'rate':
            posts = posts.order_by('rate')
        if order == '-rate':
            posts = posts.order_by('-rate')
        max_page = posts.__len__() / settings.OBJECT_PER_PAGE

        if round(max_page) < max_page:
            max_page += 1

        else:
            max_page = round(max_page)
        page = request.GET.get('page', 1)

        start = (int(page) - 1) * settings.OBJECT_PER_PAGE
        end = (int(page)) * settings.OBJECT_PER_PAGE

        context = {
            'posts': posts[start:end],
            'max_page': range(1, int(max_page) + 1)
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


def post_update_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return render(request, '404.html')

    if request.method == 'GET':
        context = {
            'form': PostForm2(instance=post),
            'post': post,
        }
        return render(request, 'post/update.html', context=context)

    if request.method == 'POST':
        form = PostForm2(request.POST, request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('/posts/')
        else:
            context = {
                'form': form,
                'post': post,
            }
            return render(request, 'post/update.html', context=context)


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
        search = request.GET.get('search')
        order = request.GET.get('order')
        if search:
            products = products.filter(
                Q(title__icontains=search) | Q(description__icontains=search)
            )
        if order == 'date':
            products = products.order_by('created_at')
        if order == '-date':
            products = products.order_by('-created_at')
        if order == 'price':
            products = products.order_by('price')
        if order == '-price':
            products = products.order_by('-price')

        max_page = products.__len__() / settings.OBJECT_PER_PAGE

        if round(max_page) < max_page:
            max_page += 1

        else:
            max_page = round(max_page)
        page = request.GET.get('page', 1)

        start = (int(page) - 1) * settings.OBJECT_PER_PAGE
        end = (int(page)) * settings.OBJECT_PER_PAGE
        context = {
            'products': products[start:end],
            'max_page': range(1, int(max_page) + 1)
        }
        return render(request, 'product/products.html', context=context)


def product_update_view(request, post_id):
    try:
        product = Products.objects.get(id=post_id)
    except Products.DoesNotExist:
        return render(request, '404.html')

    if request.method == 'GET':
        context = {
            'form': ProductForm2(instance=product),
            'product': product,
        }
        return render(request, 'product/update.html', context=context)

    if request.method == 'POST':
        form = ProductForm2(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/products/')
        else:
            context = {
                'form': form,
                'product': product,
            }
            return render(request, 'product/update.html', context=context)


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
            form.product = product
            form.save()
            return redirect('.')
        else:
            context = {
                'form': form,
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

