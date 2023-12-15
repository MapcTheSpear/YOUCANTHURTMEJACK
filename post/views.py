"""
views.py - файл представлений приложений(вьюшек)
"""

from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
current_date = date.today()


def test_view(request):
    print(request.method)
    if request.method == 'GET':
        return HttpResponse('Testing here, uh-huh')


def hello_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def current_date_view(request):
    if request.method == 'GET':
        return HttpResponse(current_date)


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse('BYE BYE!!!!!!!')
# Create your views here.
