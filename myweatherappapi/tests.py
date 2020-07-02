from django.test import TestCase
from faker import Faker
from rest_framework.test import APIRequestFactory
from unittest.mock import MagicMock
from .services.rest import Rest

fake = Faker()


class GetWeatherTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        from .views import GetWeather
        self.GetWeather = GetWeather()

    def testNoLatShouldReturn400(self):
        request = self.factory.get('/api/v1/weather', {'lat': fake.random_number()}, format='json')
        response = self.GetWeather.as_view()(request)

        self.assertEqual(response.status_code, 400)

    def testNoLngShouldReturn400(self):
        request = self.factory.get('/api/v1/weather', {'lng': fake.random_number()}, format='json')
        response = self.GetWeather.as_view()(request)

        self.assertEqual(response.status_code, 400)

    def testShouldReturn200(self):
        rest = Rest()
        rest.get_weather = MagicMock(return_value=[])
        request = self.factory.get('/api/v1/weather', {'lat': fake.random_number(), 'lng': fake.random_number()}, format='json')
        response = self.GetWeather.as_view()(request)

        self.assertEqual(response.status_code, 200)
