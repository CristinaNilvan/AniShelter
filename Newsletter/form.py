from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Newsletter
        fields = ('email',)