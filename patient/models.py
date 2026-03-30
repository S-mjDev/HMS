from django.db import models
from django.utils import timezone
# or from .models import Patient if in the same app


# Create your models here.

class Patient(models.Model):
    # explicit ID field (primary key); Django would add this automatically,
    # but defining it allows us to reference it by name and include it in
    # serializers/views if desired.
    id = models.AutoField(primary_key=True)

    firstname = models.CharField(max_length=100)
    midname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True)
    birthday = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    consultation_date = models.DateField(null=True, blank=True)
    doctor = models.ForeignKey('doctor.Doctor', on_delete=models.SET_NULL, null=True, blank=True)
    medical_history = models.TextField()

    def __str__(self):
        return f"{self.firstname} {self.midname} {self.lastname}"

