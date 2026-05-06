from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_patients, name='search_patients'),
]