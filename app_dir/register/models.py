from django.db import models

class RainRegister(models.Model):
    """
        RainRegister model
    """
    field = models.ForeignKey('field.Field', related_name='rainregisters', on_delete=models.PROTECT)
    date = models.DateTimeField()
    millimetres = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return f'{self.field.name} Rain Register at {self.date}'
