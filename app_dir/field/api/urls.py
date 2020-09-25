from django.urls import path

from .views import (
    FieldDetailAPIView,
    FieldListAPIView,
    FieldAverageRainFallAPIView,
    ListFieldWithRainRegisterAPIView,
    ListFieldWithTotalRainRegisterAPIView
)


urlpatterns = [
    path('', FieldListAPIView.as_view(), name='field-list'),
    path('detail/<int:pk>/', FieldDetailAPIView.as_view(), name='field-detail'),
    path('fields-average-rainfall/', FieldAverageRainFallAPIView.as_view(), \
        name='field-average-rainfall'),
    path('fields-rainfall/', ListFieldWithRainRegisterAPIView.as_view(), \
        name='field-rain-destroyer'),
    path('fields-total-rainfall/', ListFieldWithTotalRainRegisterAPIView.as_view(), \
        name='field-total-rainfall')
]
