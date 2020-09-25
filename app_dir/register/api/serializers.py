from rest_framework import serializers
from ..models import RainRegister
import datetime
from django.utils.dateparse import parse_date

class RainRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RainRegister
        fields = ['date', 'millimetres']


class RainRegisterCreateSerializer(serializers.ModelSerializer):
    date_register = serializers.DateField()
    time_register = serializers.TimeField()

    class Meta:
        model = RainRegister
        fields = ['field',
            'millimetres',
            'date_register',
            'time_register'
        ]

    def create(self, validated_data):
        field = validated_data['field']
        date_register = validated_data['date_register']
        time_register = validated_data['time_register']
        millimetres = validated_data['millimetres']
        temp_date = datetime.datetime.combine(date_register, time_register)
        rain_register_obj = RainRegister(
            field=field,
            date=temp_date,
            millimetres=millimetres
        )
        rain_register_obj.save()
        return validated_data
