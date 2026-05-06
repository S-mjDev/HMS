from django import forms
from django.db.models import Q
from patient.models import Patient
from doctor.models import Doctor


class PatientSearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Search by name, address, or medical history",
        }),
        label="Search",
    )
    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.all(),
        required=False,
        empty_label="All doctors",
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Doctor",
    )
    birthday = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            "class": "form-control",
            "type": "date",
        }),
        label="Birthday",
    )
    consultation_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            "class": "form-control",
            "type": "date",
        }),
        label="Consultation Date",
    )