from django.db import models
from django.utils import timezone
# or from .models import Patient if in the same app


# Create your models here.

class Patient(models.Model):
    # explicit ID field (primary key); Django would add this automatically,
    # but defining it allows us to manage the starting patient number.
    id = models.BigAutoField(primary_key=True)

    firstname = models.CharField(max_length=100)
    midname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True)
    birthday = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    consultation_date = models.DateField(null=True, blank=True)
    doctor = models.ForeignKey('doctor.Doctor', on_delete=models.SET_NULL, null=True, blank=True)
    medical_history = models.TextField()

    def save(self, *args, **kwargs):
        if self.pk is None:
            current_max = Patient.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
            self.pk = max(current_max + 1, 3000)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.firstname} {self.midname} {self.lastname}"

