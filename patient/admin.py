from django.contrib import admin
from .models import Patient

# Register your models here.
class PatientList(admin.ModelAdmin):
    list_display = ("id", "firstname", "midname", "lastname", "address", "birthday", "age", "consultation_date", "doctor")
    search_fields = ("firstname", "lastname")

admin.site.register(Patient, PatientList)



