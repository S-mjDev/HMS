from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_patient, name='patient_register'),
    path('list/', views.patient_list, name='patient_list'),
]