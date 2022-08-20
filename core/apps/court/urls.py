from django.urls import path

from .views import ListCourtsView

urlpatterns = [
    path('courts', ListCourtsView.as_view())
]
