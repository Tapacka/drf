from email.policy import default
from tkinter import CASCADE
from django.db import models
from sqlalchemy import ForeignKey

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):    
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)


class Measurement(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name= 'measure')




