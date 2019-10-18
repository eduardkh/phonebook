from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.


def phone_list(request):
    title = 'Welcome to my Phonebook App'
    querryset = Contact.objects.all()
    context = {
        'title': title,
        'querryset': querryset,
    }
    return render(request, 'index.html', context)


def phone_detail(request, pk):
    title = 'Contact detail'
    context = {
        'title': title,
        'contact': get_object_or_404(Contact, pk=pk),
        'phone': get_object_or_404(Phone, pk=pk),
        'email': get_object_or_404(Email, pk=pk),
    }
    return render(request, 'detail.html', context)


def phone_create(request):
    title = 'Create Contact'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        # pre-save
        instance.save()

    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'create.html', context)


def phone_update(request):
    return HttpResponse('<h1>phone_update</h1>')


def phone_delete(request):
    return HttpResponse('<h1>phone_delete</h1>')
