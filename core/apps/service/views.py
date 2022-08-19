from rest_framework.views import APIview
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .serializers import ServiceSerializers

from .models import Service

class ListServicesView(APIview):
    permissions_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Service.objects.all().exists():
            services = Service.objects.all()
            services = ServiceSerializers(services)
            return Response({'services': services.data}, status=status.HTTP_200_OK)
        else: 
            return Response({'error': 'No services found'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
