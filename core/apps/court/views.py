from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .serializers import CourtSerializers

from .models import Court


class ListCourtsView(APIView):
    permissions_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        response = {'error': 'No courts found'}
        stat = status.HTTP_500_INTERNAL_SERVER_ERROR
        if Court.objects.all().exists():
            courts = Court.objects.all()
            courts = CourtSerializers(courts, many=True)
            response = {'court': courts.data}
            stat = status.HTTP_200_OK
        return Response(response, status=stat)
