from django.views import generic
from .models import News


class PostNews(generic.ListView):
    queryset = News.objects.filter(status=1).order_by('-date')

    context_object_name = "news_query"

    template_name = 'news.html'


class PostNewsDetails(generic.DetailView):
    model = News

    template_name = 'news_details.html'




