from django.db import models


# Create your models here.


class SearchPatient(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstname} {self.midname} {self.lastname}"