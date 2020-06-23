from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import *
from .forms import *
# Create your views here.


def phone_list(request):
    title = 'Contact list'
    queryset_list = Contact.objects.all()
    # for simple Search Form
    query = request.GET.get('q')
    if query:
        query = query.strip().split()
        queryset_list = queryset_list.filter(
            Q(company__icontains=query[0]) |
            Q(job_title__icontains=query[0]) |
            Q(first_name__icontains=query[0]) |
            Q(last_name__icontains=query[0]) |
            Q(notes__icontains=query[0])
        ).distinct()
    paginator = Paginator(queryset_list, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    last_page = str(paginator.page(paginator.num_pages)).split(' ')[1]

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        'title': title,
        'queryset': queryset,
        'page_request_var': page_request_var,
        'last_page': last_page,
    }
    return render(request, 'list.html', context)


def phone_detail(request, pk):
    title = 'Contact detail'
    contact = get_object_or_404(Contact, pk=pk)
    phones = contact.phone_set.all()
    emails = contact.email_set.all()
    context = {
        'title': title,
        'contact': contact,
        'phones': phones,
        'emails': emails,
    }
    return render(request, 'detail.html', context)


def phone_create(request):
    title = 'Contact Create'
    form = ContactForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print(request.POST)
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
