from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime


class GetWeather(APIView):
    from .services.rest import Rest
    from .services.aggregator import Aggregator

    def _build_response(self, hourly_temperatures):
        return {
            'min_temp': self.Aggregator().aggregate_min_temp(hourly_temperatures),
            'max_temp': self.Aggregator().aggregate_max_temp(hourly_temperatures),
            'avg_temp': self.Aggregator().aggregate_average_temp(hourly_temperatures),
            'median_temp': self.Aggregator().aggregate_median_temp(hourly_temperatures),
            'min_humidity': self.Aggregator().aggregate_min_humidity(hourly_temperatures),
            'max_humidity': self.Aggregator().aggregate_max_humidity(hourly_temperatures),
            'avg_humidity': self.Aggregator().aggregate_average_humidity(hourly_temperatures),
            'median_humidity': self.Aggregator().aggregate_median_humidity(hourly_temperatures),
            'hourly_temperatures': ({'date': datetime.fromtimestamp(item.get('dt')).date(),
                                     'time': datetime.fromtimestamp(item.get('dt')).time(),
                                     'temp': item.get('temp'),
                                     'humidity': item.get('humidity')}
                                    for item in hourly_temperatures)
        }

    def get(self, request):
        city = request.GET.get('lat', None)
        date = request.GET.get('lng', None)

        if city is None or date is None:
            return JsonResponse(data={}, status=status.HTTP_400_BAD_REQUEST)

        weather = self.Rest().get_weather('26.2041', '28.0473')
        if weather is None:
            return JsonResponse(data={}, status=status.HTTP_404_NOT_FOUND)

        hourly_temperatures = weather.get('hourly')

        return Response(data=self._build_response(hourly_temperatures), status=status.HTTP_200_OK)
