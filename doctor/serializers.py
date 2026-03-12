from rest_framework import serializers
from doctor.models import Doctor

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ["url", "id", "firstname", "midname", "lastname", "specialization"]