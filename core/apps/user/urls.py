from django.urls import path
from apps.user.views import (UserCreateAPIView, ListUsersAPIView)

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='user_create'),
    path('users/', ListUsersAPIView.as_view(), name='list_users')
]
