from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Contact)
# admin.site.register(Phone)
# admin.site.register(Email)


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['pk', 'author', 'first_name', 'last_name']
    list_display_links = ['pk']
    search_fields = ['first_name', 'last_name']

    class Meta:
        model = Contact


class PhoneModelAdmin(admin.ModelAdmin):
    list_display = ['pk', 'phone', 'contact']
    list_display_links = ['pk']
    search_fields = ['phone', 'contact']

    class Meta:
        model = Phone


class EmailModelAdmin(admin.ModelAdmin):
    list_display = ['pk', 'email', 'contact']
    list_display_links = ['pk']
    search_fields = ['email', 'contact']

    class Meta:
        model = Email


admin.site.register(Contact, ContactModelAdmin)
admin.site.register(Phone, PhoneModelAdmin)
admin.site.register(Email, EmailModelAdmin)
