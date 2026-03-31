from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.register_patient, name='patient_register'),
    path('list/', views.patient_list, name='patient_list'),
=======
    path('', views.patient, name='patient'),
>>>>>>> 507d7d53ae00c78e08bb362c85ad854ae7affc73
]