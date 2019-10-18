from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.


def phone_list(request):
    title = 'Contact list'
    querryset = Contact.objects.all()
    context = {
        'title': title,
        'querryset': querryset,
    }
    return render(request, 'list.html', context)


def phone_detail(request, pk):
    title = 'Contact detail'
    context = {
        'title': title,
        'contact': get_object_or_404(Contact, pk=pk)
    }
    return render(request, 'detail.html', context)


def phone_create(request):
    title = 'Contact Create'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        # pre-save
        instance.save()
        messages.success(request, 'Contact Created')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'create.html', context)


def phone_update(request, pk=None):
    title = 'Contact Edit'
    instance = get_object_or_404(Contact, pk=pk)
    form = ContactForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Contact Updated')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'title': title,
        'instance': instance,
        'form': form,
    }
    return render(request, 'create.html', context)


def phone_delete(request, pk=None):
    instance = get_object_or_404(Contact, pk=pk)
    instance.delete()
    messages.success(request, 'Contact Deleted')
    return redirect('phone:phone_list')
