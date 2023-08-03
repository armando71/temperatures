from django.db import models
from django.utils import timezone

# Create your models here.
class AbstractName(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        abstract = True

class AbstractAt(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    class Meta:
        abstract = True

class Area(AbstractName, AbstractAt):
    owner = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.EmailField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name

class Region(AbstractName, AbstractAt):
    area = models.ForeignKey(Area, related_name='region_area', on_delete=models.CASCADE)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.area}"

class Measurements(AbstractAt):
    region = models.ForeignKey(Region, related_name='region', on_delete=models.CASCADE)
    temperature = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.region}"
