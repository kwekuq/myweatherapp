from .views import GetWeather
from django.urls import path

urlpatterns = [
    path('weather/', GetWeather.as_view()),
]