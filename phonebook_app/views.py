from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def phone_list(request):
    return HttpResponse('<h1>phone_list</h1>')


def phone_detail(request):
    return HttpResponse('<h1>phone_detail</h1>')


def phone_create(request):
    return HttpResponse('<h1>phone_create</h1>')


def phone_update(request):
    return HttpResponse('<h1>phone_update</h1>')


def phone_delete(request):
    return HttpResponse('<h1>phone_delete</h1>')
