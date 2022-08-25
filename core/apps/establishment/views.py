from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissions

from apps.establishment.models import Establishment
from apps.establishment.serializers import EstablishmentSerializer


class CreateEstablishmentAPIView(generics.ListCreateAPIView):
    queryset = Establishment.objects.all()
    permission_classes = (DjangoModelPermissions,)

    def create(self, request, format=None):
        data = request.data
        establishment_serializer = EstablishmentSerializer(data=data)
        if establishment_serializer.is_valid():
            establishment_serializer.save()
            return Response({
                'message': 'Establishment created successfully',
            }, status.HTTP_201_CREATED)
        return Response({
            'message': 'Register has errors',
            'errors': establishment_serializer.errors
        }, status.HTTP_400_BAD_REQUEST)
