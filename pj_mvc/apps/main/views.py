from django.shortcuts import render
# Django
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Main page</h1>')


def get_number2(request):
    return HttpResponse('<h1>2</h1>')