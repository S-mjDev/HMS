from django.urls import path
from . import views

urlpatterns = [
    path('', views.DoctorViewSet.as_view({'get': 'list'}), name='doctor-list'),
    path('<int:pk>/', views.DoctorViewSet.as_view({'get': 'retrieve'}), name='doctor-detail'),
]