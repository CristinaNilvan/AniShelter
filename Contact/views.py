from django.shortcuts import render
from django.views import generic
from .form import ContactForm
from .models import Contact


class ContactView(generic.TemplateView):
    template_name = 'contact.html'
    final_template_name = 'contact_response.html'
    registered_template_name = 'contact_registered_response.html'

    def get(self, request, **kwargs):
        form = ContactForm

        args = {'form': form}

        return render(request, self.template_name, args)

    @staticmethod
    def validate_save(database_name, database_object):

        if database_name.objects.filter(last_name=database_object.last_name).exists() and \
                database_name.objects.filter(first_name=database_object.first_name).exists() and \
                database_name.objects.filter(email=database_object.email).exists() and \
                database_name.objects.filter(message=database_object.message).exists():
            return False

        return True

    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():

            database_object = form.save(commit=False)

            if self.validate_save(Contact, database_object):
                form.save()

                return render(request, self.final_template_name)

            else:

                return render(request, self.registered_template_name)
