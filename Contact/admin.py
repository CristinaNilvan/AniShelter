from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'last_name', 'first_name', 'date')


admin.site.register(Contact, ContactAdmin)
