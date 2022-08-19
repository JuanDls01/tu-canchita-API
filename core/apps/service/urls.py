from django.urls import path

from .views import ListServicesView

urlpatterns = [
    path('services', ListServicesView.as_view())
]