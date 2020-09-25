from django.db import models
from .managers import FieldManager
from datetime import datetime, timedelta
from django.db.models import Avg, Sum


class Field(models.Model):
    """
        Field model
    """
    name = models.CharField(max_length=255)
    hectare = models.PositiveIntegerField(default=0)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)

    objects = models.Manager()
    filter_objects = FieldManager()

    def __str__(self):
        return f'{self.name}'

    def get_field_average_rainfall(self, days):
        average = self.rainregisters\
            .filter(date__gte=datetime.now()-timedelta(days=days))\
            .aggregate(Avg('millimetres'))\
            .get('millimetres__avg')
        if average:
            return average
        else:
            return 0

    def get_field_sum_rainfall(self):
        total = self.rainregisters\
            .aggregate(Sum('millimetres'))\
            .get('millimetres__sum')
        if total:
            return total
        else:
            return 0

