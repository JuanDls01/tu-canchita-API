from rest_framework import serializers
from .models import Service


class ServiceSerializers(serializers.ModelSerialzier):
    class Meta:
        model = Service
        fields = [
            'id',
            'name',
        ]
