from django.contrib.auth.models import Group, User
from patient.models import Patient
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        # expose the primary key so clients can see the record ID
        fields = ["url", "id", "firstname", "midname", "lastname", "address", "birthday", "age", "consultation_date", "doctor", "medical_history"]

