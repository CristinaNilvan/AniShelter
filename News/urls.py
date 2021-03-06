from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.PostNews.as_view(), name='news'),
    path('news/<slug:news_slug>', views.PostNewsDetails.as_view(), name='news_details')
]