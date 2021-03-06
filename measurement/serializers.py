from rest_framework import serializers

from measurement.models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']


class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'sensor']        

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields =  ['id', 'name', 'description']  


class SensorDetailSerializer(serializers.ModelSerializer):
    measure = MeasurementSerializer(read_only=True, many = True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measure']
