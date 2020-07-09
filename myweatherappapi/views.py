from datetime import datetime

from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class GetWeather(APIView):
    from .services.rest import Rest
    from .services.aggregator import Aggregator

    def _build_graph_data_model(self, hourly_temperatures):
        data_sets = [{
            'label': 'Temp',
            'fill': False,
            'borderColor': '#e84118',
            'data': list(self.Aggregator()._convert_kelvin_to_celsius(item.get('temp')) for item in hourly_temperatures[0:12])
        }, {
            'label': 'Humidity',
            'fill': False,
            'borderColor': '#0097e6',
            'data': list(item.get('humidity') for item in hourly_temperatures[0:12])
        }]
        return {
            'labels': (datetime.fromtimestamp(item.get('dt')).time() for item in hourly_temperatures[0:12]),
            'datasets': data_sets
        }

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
            'hourly_temperatures': self._build_graph_data_model(hourly_temperatures)
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
