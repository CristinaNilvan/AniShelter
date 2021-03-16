from django.db import models
from .models_data_structures import *


class Vaccine(models.Model):
    name = models.CharField(max_length=50, default="Not necessary")
    times_per_year = models.IntegerField(blank=False)

    def __str__(self):
        return self.name


class Animal(models.Model):
    animal_id = models.CharField(max_length=25, blank=False, unique=True)
    name = models.CharField(max_length=50, blank=False)
    age = models.IntegerField(blank=False)
    gender = models.CharField(max_length=6, choices=GENDER, default="Not picked yet")
    animal_type = models.CharField(max_length=30, choices=ANIMALS_TYPES, default="Not picked yet")
    condition = models.CharField(max_length=10, choices=ANIMAL_CONDITION, default="Not picked yet")
    health_status = models.BooleanField(default=True)
    vaccines = models.ManyToManyField(Vaccine)
    adoption_status = models.BooleanField(default=False)
    story = models.TextField(blank=False)
    picture = models.ImageField(upload_to="animals_pictures/", default="default.jpg")

    def __str__(self):
        return self.animal_id


