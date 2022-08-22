# from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from apps.user.models import UserAccount
# from django.contrib.auth import get_user_model
# User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'

    def create(self, validated_data):
        user = UserAccount(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
