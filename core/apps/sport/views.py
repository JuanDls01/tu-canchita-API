from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .serializers import SportSerializer


from .models import Sport


class ListSportsView(APIView):
    permissions_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Sport.objects.all().exists():
            sports = Sport.objects.all()
            sports = SportSerializer(sports, many=True)
            return Response({'sports': sports.data}, status=status.HTTP_200_OK)

        else:
            return Response({'error': 'No sports found'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
