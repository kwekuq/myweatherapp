from django.test import TestCase
from faker import Faker
from rest_framework.test import APIRequestFactory

fake = Faker()


class GetWeatherTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        from .views import GetWeather
        self.GetWeather = GetWeather()

    def testNoCityShouldReturn400(self):
        request = self.factory.get('/api/v1/weather', {'date': fake.date()}, format='json')
        response = self.GetWeather.as_view()(request)

        self.assertEqual(response.status_code, 400)

    def testNoDateShouldReturn400(self):
        request = self.factory.get('/api/v1/weather', {'city': fake.name()}, format='json')
        response = self.GetWeather.as_view()(request)

        self.assertEqual(response.status_code, 400)

    def testShouldReturn200(self):
        request = self.factory.get('/api/v1/weather', {'city': fake.name(), 'date': fake.date()}, format='json')
        response = self.GetWeather.as_view()(request)

        self.assertEqual(response.status_code, 200)
