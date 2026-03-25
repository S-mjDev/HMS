from django.urls import path
from . import views

urlpatterns = [
    path('', views.Patient, name='patient'),
    path('template/', views.Patient, name='patient_template'),
]