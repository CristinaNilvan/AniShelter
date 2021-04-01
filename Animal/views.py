from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from .models import Animal


def index(request):
    template_name = 'index.html'

    animal_query = Animal.objects.filter(adoption_status=False)[:3]

    context = {'animal_query': animal_query}

    return render(request, template_name, context)


class AnimalList(LoginRequiredMixin, generic.ListView):
    queryset = Animal.objects.filter(adoption_status=False)

    context_object_name = "animal_query"

    template_name = 'animal_list.html'


class AnimalListDetails(LoginRequiredMixin, generic.DetailView):
    model = Animal

    template_name = 'animal_list_details.html'

    slug_field = "animal_slug"
    slug_url_kwarg = "animal_slug"
