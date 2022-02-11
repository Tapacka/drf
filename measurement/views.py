# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer, MeasurementsSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView




class DemoView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        new_sensor = Sensor(name=self.request.data["name"], description=self.request.data['description'])
        new_sensor.save()
        return Response({'status': 'OK'})

    

class UpdateView(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    

class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementsSerializer



class SensorDetailView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
