from django.urls import path

from measurement.views import DemoView, SensorDetailView, UpdateView, MeasurementCreateView, MeasurementListView


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', DemoView.as_view()),
    path('sensors/<pk>/', UpdateView.as_view()),
    path('sensor/<pk>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
    path('measurement/', MeasurementListView.as_view()),
]
