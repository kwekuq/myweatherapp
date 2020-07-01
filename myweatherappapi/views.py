from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView


class GetWeather(APIView):

    def get(self, request):
        city = request.GET.get('city', None)
        date = request.GET.get('date', None)

        if city is None or date is None:
            return JsonResponse(data={}, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse(data={})
