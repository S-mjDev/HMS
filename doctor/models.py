from django.db import models

# Create your models here.

class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    midname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    specialization = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Dr. {self.firstname} {self.midname} {self.lastname} - {self.specialization}"
