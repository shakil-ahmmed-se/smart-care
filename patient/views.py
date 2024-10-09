from django.shortcuts import render

from rest_framework import viewsets
from .models import Patient
from .import serializers
# Create your views here.

class PatientViewset(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = serializers.PatientSerializer