from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status

# Aca voy a poner las vistas de establecimiento, todavía falta pensar como voy a mostrar en el inicio


class CreateEstablishmentView(APIView):
    permision_classes = [permissions.Is]

    def post(self, request, format=None):
        pass
