from rest_framework.generics import (
    RetrieveAPIView, ListAPIView
)
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from .serializers import FieldSerializer, \
    FieldAverageRainFallSerializer, \
    ListFieldAverageRainFallSerializer, \
    ListFieldWithRainRegisterSerializer, \
    FieldTotalRainFallSerializer, \
    ListFieldTotalRainFallSerializer
from ..models import Field


class FieldDetailAPIView(RetrieveAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


class FieldListAPIView(ListAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


class FieldAverageRainFallAPIView(APIView):

    def get(self, request, format=None):
        """
            Returns a list of fiels with average rainfall
        """
        status_response = status.HTTP_200_OK
        content = {}
        field_serializer = FieldAverageRainFallSerializer(
            data={'days': request.data.get('days')}
            )
        if field_serializer.is_valid(raise_exception=True):
            fields = Field.objects.all()
            serializer = ListFieldAverageRainFallSerializer(fields, many=True, \
                context={'days': request.data.get('days')})
            content = serializer.data
            status_response = status.HTTP_200_OK

        return Response(content, status=status_response)


class ListFieldWithRainRegisterAPIView(ListAPIView):
    queryset = Field.objects.all()
    serializer_class = ListFieldWithRainRegisterSerializer


class ListFieldWithTotalRainRegisterAPIView(APIView):

    def get(self, request, format=None):
        status_response = status.HTTP_200_OK
        content = {}
        field_serializer = FieldTotalRainFallSerializer(
            data={'total_millimetres': request.data.get('total_millimetres')}
            )
        if field_serializer.is_valid(raise_exception=True):
            fields = Field.filter_objects.filters_less_rainfall(\
                request.data.get('total_millimetres'))
            serializer = ListFieldTotalRainFallSerializer(fields, many=True)
            content = serializer.data
            status_response = status.HTTP_200_OK

        return Response(content, status=status_response)