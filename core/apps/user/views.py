from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.user.models import UserAccount
from apps.user.serializers import (UserSerializer, CustomUserSerializer)


class UserCreateAPIView(generics.CreateAPIView):
    def create(self, request):
        data = request.data
        user_serializer = UserSerializer(data=data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'User created successfully',
            }, status.HTTP_201_CREATED)

        return Response({
            'message': 'Hay errores en el registro',
            'errors': user_serializer.errors
        }, status.HTTP_400_BAD_REQUEST)


class ListUsersAPIView(generics.ListAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CustomUserSerializer(queryset, many=True)
        return Response({
            'users': serializer.data
        }, status.HTTP_200_OK)
