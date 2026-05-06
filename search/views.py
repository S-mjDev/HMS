from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.db.models import Q
from patient.models import Patient
from .forms import PatientSearchForm


class Search(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)


def search_patients(request):
    form = PatientSearchForm(request.GET or None)
    patients = Patient.objects.all().order_by("id")

    if form.is_valid():
        query = form.cleaned_data.get("query", "").strip()
        doctor = form.cleaned_data.get("doctor")
        birthday = form.cleaned_data.get("birthday")
        consultation_date = form.cleaned_data.get("consultation_date")

        if query:
            patients = patients.filter(
                Q(firstname__icontains=query)
                | Q(midname__icontains=query)
                | Q(lastname__icontains=query)
                | Q(address__icontains=query)
                | Q(medical_history__icontains=query)
            )

        if doctor:
            patients = patients.filter(doctor=doctor)

        if birthday:
            patients = patients.filter(birthday=birthday)

        if consultation_date:
            patients = patients.filter(consultation_date=consultation_date)

    return render(request, "search.html", {"form": form, "patients": patients})