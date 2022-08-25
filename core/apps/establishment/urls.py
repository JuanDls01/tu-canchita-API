from django.urls import path
from apps.establishment.views import CreateEstablishmentAPIView

urlpatterns = [
    path('create/', CreateEstablishmentAPIView.as_view(),
         name='create-establishment'),
]
