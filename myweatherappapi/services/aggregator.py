import json
from operator import attrgetter
import statistics


class Aggregator:
    def aggregate_min_temp(self, temperatures):
        return self._get_min(temperatures, 'temp')

    def aggregate_max_temp(self, temperatures):
        return self._get_max(temperatures, 'temp')

    def aggregate_average_temp(self, temperatures):
        return self._get_average(temperatures, 'temp')

    def aggregate_median_temp(self, temperatures):
        return self._get_median(temperatures, 'temp')

    def aggregate_min_humidity(self, temperatures):
        return self._get_min(temperatures, 'humidity')

    def aggregate_max_humidity(self, temperatures):
        return self._get_max(temperatures, 'humidity')

    def aggregate_average_humidity(self, temperatures):
        return self._get_average(temperatures, 'humidity')

    def aggregate_median_humidity(self, temperatures):
        return self._get_median(temperatures, 'humidity')

    @staticmethod
    def _get_min(obj_list, field):
        return round(min(item.get(field) for item in obj_list), 2)

    @staticmethod
    def _get_max(obj_list, field):
        return round(max(item.get(field) for item in obj_list), 2)

    @staticmethod
    def _get_average(obj_list, field):
        return round(statistics.mean((item.get(field) for item in obj_list)), 2)

    @staticmethod
    def _get_median(obj_list, field):
        return round(statistics.median((item.get(field) for item in obj_list)), 2)
