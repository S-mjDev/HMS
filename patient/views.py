from urllib.request import Request

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.views import View
from patient.models import Patient
from patient.forms import PatientRegistrationForm
from rest_framework import permissions, viewsets
from django.template import loader


from patient.serializers import GroupSerializer, UserSerializer, PatientSerializer


def register_patient(request):
    if request.method == "POST":
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient registered successfully.")
            # Redirect to patient list (change below if a different landing page is desired)
            return redirect("patient_list")
    else:
        form = PatientRegistrationForm()

    return render(request, "patient_registration.html", {"form": form})


def patient_list(request):
    patients = Patient.objects.all().order_by("id")
    return render(request, "patient_list.html", {"patients": patients})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class PatientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows patients to be viewed or edited.
    """

    queryset = Patient.objects.all().order_by("id")
    serializer_class = PatientSerializer
    permission_classes = []  # Temporarily remove authentication for development




