from django import forms
from .models import Contact, Phone, Email


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'image',
            'notes'
        ]
