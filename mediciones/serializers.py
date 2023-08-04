from rest_framework import serializers

from .models import Area, Region, Measurements

class AreaSerializar(serializers.ModelSerializer):
    class Meta:
        model = Area
        # fields = ['id', 'name', 'owner', ] Para campos individuales
        fields = '__all__' # Para todos los campos del modelo

class RegionSerializar(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class MeasurementsSerializar(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = '__all__'