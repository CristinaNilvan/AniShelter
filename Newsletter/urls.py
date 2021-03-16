from django.urls import path
from . import views

urlpatterns = [
    path('newsletter/', views.NewsletterView.as_view(), name='newsletter'),
]