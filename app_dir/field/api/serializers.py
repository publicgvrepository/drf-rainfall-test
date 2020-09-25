from rest_framework import serializers
from ..models import Field
from app_dir.register.api.serializers import RainRegisterSerializer

MAX_DAYS_AVERAGE = 7

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'


class FieldAverageRainFallSerializer(serializers.Serializer):
    """
    Request user can be Inviter at stage
    """
    days = serializers.IntegerField()

    def validate(self, data):
        """
        Must check 'days' is valid
        """
        days = data.get('days')
        try:
            if 0 < days <= MAX_DAYS_AVERAGE:
                return data
            else:
                raise serializers.ValidationError("Days must be between 1 and 7")
        except:
            raise serializers.ValidationError("You must specify valid days data")


class FieldTotalRainFallSerializer(serializers.Serializer):
    """
    Request user can be Inviter at stage
    """
    total_millimetres = serializers.DecimalField(max_digits=6, decimal_places=3)

    def validate(self, data):
        """
        Must check 'days' is valid
        """
        total_millimetres = data.get('total_millimetres')
        try:
            if 0 < total_millimetres:
                return data
            else:
                raise serializers.ValidationError("Millimetres must be bigger than 0")
        except:
            raise serializers.ValidationError("You must specify valid millimetres data")


class ListFieldAverageRainFallSerializer(FieldSerializer):
    average_rainfall = serializers.SerializerMethodField()

    def get_average_rainfall(self, obj):
        average = obj.get_field_average_rainfall(self.context.get('days'))
        return str(average)


class ListFieldWithRainRegisterSerializer(serializers.ModelSerializer):
    rainregisters = RainRegisterSerializer(many=True, read_only=True)

    class Meta:
        model = Field
        fields = ['name', 'rainregisters']


class ListFieldTotalRainFallSerializer(FieldSerializer):
    total_rainfall = serializers.SerializerMethodField()

    def get_total_rainfall(self, obj):
        total = obj.get_field_sum_rainfall()
        return str(total)
