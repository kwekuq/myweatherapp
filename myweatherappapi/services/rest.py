import requests
from rest_framework import status
from django.conf import settings


class Rest:
    def __init__(self):
        self.api_key = settings.OPENWEATHERMAP_API

    def get_weather(self, lat, lng):
        url = F'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lng}&appid={self.api_key}'
        response = requests.get(url)
        if response.status_code is status.HTTP_200_OK:
            return response.json()
        return None
