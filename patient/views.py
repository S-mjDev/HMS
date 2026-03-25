from urllib.request import Request

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import Group, User
from django.views import View
from patient.models import Patient
from rest_framework import permissions, viewsets
from django.template import loader


from patient.serializers import GroupSerializer, UserSerializer, PatientSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class PatientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows patients to be viewed or edited.
    """

    queryset = Patient.objects.all().order_by("id")
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

def home(APIView):
        templates = loader.get_template("home.html")
        return HttpResponse(templates.render())


