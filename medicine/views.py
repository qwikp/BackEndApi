from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Medicine
from . import serializers

class MedicineViewset(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = serializers.MedicineSerializer
