from django.contrib import admin
from .models import Animal, Vaccine


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('animal_id', 'name', 'gender', 'health_status', 'adoption_status')


class VaccineAdmin(admin.ModelAdmin):
    list_display = ('name', 'times_per_year')


admin.site.register(Animal, AnimalAdmin)
admin.site.register(Vaccine, VaccineAdmin)

admin.site.site_header = "AnimalShelter Control Panel"
