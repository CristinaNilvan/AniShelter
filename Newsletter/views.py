from django.shortcuts import render
from django.views import generic
from .form import NewsletterForm
from .models import Newsletter


class NewsletterView(generic.TemplateView):
    template_name = 'newsletter.html'
    final_template_name = 'newsletter_response.html'
    registered_template_name = 'newsletter_registered_response.html'

    def get(self, request, **kwargs):
        form = NewsletterForm

        args = {'form': form}

        return render(request, self.template_name, args)

    @staticmethod
    def validate_save(database_name, database_object):

        if database_name.objects.filter(email=database_object.email).exists():
            return False

        return True

    def post(self, request):
        form = NewsletterForm(request.POST)

        if form.is_valid():

            database_object = form.save(commit=False)

            if self.validate_save(Newsletter, database_object):
                form.save()

                return render(request, self.final_template_name)

            else:

                return render(request, self.registered_template_name)
