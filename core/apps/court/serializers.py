from rest_framework import serializers
from .models import Court


class CourtSerializers(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = '__all__'
