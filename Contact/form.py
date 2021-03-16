from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    last_name = forms.CharField()
    first_name = forms.CharField()
    email = forms.EmailField()
    message = forms.Textarea()

    class Meta:
        model = Contact
        fields = ('last_name', 'first_name', 'email', 'message')
