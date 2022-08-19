from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),

    path('api/sport/', include('apps.sport.urls')),
    path('api/service/', include('apps.service.urls')),
    path('api/establishment/', include('apps.establishment.urls')),
    path('api/court/', include('apps.court.urls')),
]
