from django.shortcuts import render
from rest_framework import generics

from .models import Area, Region, Measurements

from .serializers import AreaSerializar, RegionSerializar, MeasurementsSerializar

# Create your views here.

class AreaAPIListView(generics.ListAPIView):
    serializer_class = AreaSerializar
    queryset = Area.objects.all()

class AreaAPICreateView(generics.CreateAPIView):
    serializer_class = AreaSerializar
    queryset = Area.objects.all()

class RegionAPIListView(generics.ListAPIView):
    serializer_class = RegionSerializar
    queryset = Region.objects.all()

class RegionAPICreateView(generics.CreateAPIView):
    serializer_class = RegionSerializar
    queryset = Region.objects.all()

class MeasurementsAPIListView(generics.ListAPIView):
    serializer_class = MeasurementsSerializar
    queryset = Measurements.objects.all()

class MeasurementsAPICreateView(generics.CreateAPIView):
    serializer_class = MeasurementsSerializar
    queryset = Measurements.objects.all()