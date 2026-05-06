from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('home', views.home, name='home'),
    path('register/', views.register_patient, name='patient_register'),
]