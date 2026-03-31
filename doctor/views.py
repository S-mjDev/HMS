from django.shortcuts import render
from django.http import HttpResponse
from doctor.models import Doctor
from doctor.serializers import DoctorSerializer
from rest_framework import permissions, viewsets

# Create your views here.
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by("id")
    serializer_class = DoctorSerializer
<<<<<<< HEAD
    permission_classes = []  # Temporarily remove authentication for development
=======
    permission_classes = [permissions.IsAuthenticated]
>>>>>>> 507d7d53ae00c78e08bb362c85ad854ae7affc73
