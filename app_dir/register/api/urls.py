from django.urls import path

from .views import (
    RainRegisterCreateAPIView,
)

urlpatterns = [
    path('create/rainfall', RainRegisterCreateAPIView.as_view(), name='rain-register-creator')
]
