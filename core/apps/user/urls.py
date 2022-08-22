from django.urls import path
from apps.user.views import UserCreateAPIView

urlpatterns = [
    path('users/', UserCreateAPIView.as_view(), name='user_create')
]
