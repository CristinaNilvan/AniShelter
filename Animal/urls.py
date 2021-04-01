from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('animal-list/', views.AnimalList.as_view(), name='animal_list'),
    path('animal-list/<slug:animal_slug>', views.AnimalListDetails.as_view(), name='animal_list_details'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

