from typing import List
from django.urls import path

from .views import ListSportsView

urlpatterns = [
    path('sports', ListSportsView.as_view()),
]
