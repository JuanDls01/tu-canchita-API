from djoser.serializers import UserCreateSerelizer
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UserCreateSerializer(UserCreateSerelizer):
    class Meta(UserCreateSerelizer.Meta):
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'get_full_name',
            'get_short_name',
        )
