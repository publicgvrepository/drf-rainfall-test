from django.db import models


class FieldManager(models.Manager):

    def filters_less_rainfall(self, minimum_value):
        fields_filtered = list(\
            map(lambda x: x.id,\
                (filter(lambda x: x.get_field_sum_rainfall() < minimum_value, self.get_queryset()))))
        return self.get_queryset().exclude(id__in=fields_filtered)