from rest_framework.generics import (
    CreateAPIView
)
from .serializers import RainRegisterCreateSerializer
from ..models import RainRegister


class RainRegisterCreateAPIView(CreateAPIView):
    serializer_class = RainRegisterCreateSerializer
    queryset = RainRegister.objects.all()