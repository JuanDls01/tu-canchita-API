from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from apps.user.serializers import UserCreateSerializer


class UserCreateAPIView(generics.ListCreateAPIView):
    permissions_classes = (permissions.AllowAny,)

    def create(self, request):
        data = request.data
        user_serializer = UserCreateSerializer(data=data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'User created successfully',
                'user': user_serializer.data
            }, status.HTTP_201_CREATED)

        return Response({
            'message': 'Hay errores en el registro',
            'errors': user_serializer.errors
        }, status.HTTP_400_BAD_REQUEST)
