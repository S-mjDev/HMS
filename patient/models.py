from django.db import models
# or from .models import Patient if in the same app


# Create your models here.

class Patient(models.Model):
    firstname = models.CharField(max_length=100)
    midname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    medical_history = models.TextField()

    def __str__(self):
        return f"{self.firstname} {self.midname} {self.lastname}"