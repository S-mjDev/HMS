from urllib.request import Request

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.views import View
from django.db.models import Q
from patient.models import Patient
from doctor.models import Doctor
from patient.forms import PatientRegistrationForm
from rest_framework import permissions, viewsets
from django.template import loader
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


from patient.serializers import GroupSerializer, UserSerializer, PatientSerializer

def home(request):
    return render(request, "home.html", {"title": "Home"})
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
    query = request.GET.get("q", "").strip()
    doctor_id = request.GET.get("doctor", "").strip()
    birthday = request.GET.get("birthday", "").strip()
    consultation_date = request.GET.get("consultation_date", "").strip()

    if query:
        patients = patients.filter(
            Q(firstname__icontains=query)
            | Q(midname__icontains=query)
            | Q(lastname__icontains=query)
            | Q(address__icontains=query)
            | Q(medical_history__icontains=query)
        )

    selected_doctor_name = ""
    if doctor_id.isdigit():
        patients = patients.filter(doctor__id=int(doctor_id))
        selected_doctor = Doctor.objects.filter(id=int(doctor_id)).first()
        if selected_doctor:
            selected_doctor_name = str(selected_doctor)

    if birthday:
        patients = patients.filter(birthday=birthday)

    if consultation_date:
        patients = patients.filter(consultation_date=consultation_date)

    doctors = Doctor.objects.all().order_by("lastname")
    return render(
        request,
        "patient_list.html",
        {
            "patients": patients,
            "doctors": doctors,
            "selected_doctor_name": selected_doctor_name,
        },
    )


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
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['firstname', 'midname', 'lastname', 'birthday']
    search_fields = ['firstname', 'midname', 'lastname', 'address', 'medical_history']




