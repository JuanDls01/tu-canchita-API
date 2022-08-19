from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .serializers import ServiceSerializer

from .models import Service


class ListServicesView(APIView):
    permissions_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Service.objects.all().exists():
            services = Service.objects.all()
            services = ServiceSerializer(services, many=True)
            return Response({'services': services.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No services found'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
