from django.contrib import admin
from .models import Doctor

# Register your models here.
class DoctorList(admin.ModelAdmin):
    list_display = ("id", "firstname", "midname", "lastname", "specialization")
    search_fields = ("firstname", "lastname")

admin.site.register(Doctor, DoctorList)
