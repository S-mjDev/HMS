from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Patient


class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            "firstname",
            "midname",
            "lastname",
            "address",
            "birthday",
            "age",
            "consultation_date",
            "doctor",
            "medical_history",
        ]
        widgets = {
            "firstname": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "First name",
            }),
            "midname": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Middle name",
            }),
            "lastname": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Last name",
            }),
            "address": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Address",
            }),
            "birthday": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
            }),
            "age": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Age",
            }),
            "consultation_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
            }),
            "doctor": forms.Select(attrs={
                "class": "form-select",
            }),
            "medical_history": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Medical history or notes",
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        firstname = cleaned_data.get("firstname")
        midname = cleaned_data.get("midname")
        lastname = cleaned_data.get("lastname")
        birthday = cleaned_data.get("birthday")

        # If we have at least name data and optionally birthday, check if patient exists
        if firstname and lastname:
            candidate = Patient.objects.filter(
                firstname__iexact=firstname.strip(),
                lastname__iexact=lastname.strip(),
            )

            if midname:
                candidate = candidate.filter(midname__iexact=midname.strip())

            if birthday:
                candidate = candidate.filter(birthday=birthday)

            if self.instance and self.instance.pk:
                candidate = candidate.exclude(pk=self.instance.pk)

            if candidate.exists():
                raise forms.ValidationError(
                    _("Patient already exists with the same name and birthday. Please check the record or update the existing patient.")
                )

        return cleaned_data
