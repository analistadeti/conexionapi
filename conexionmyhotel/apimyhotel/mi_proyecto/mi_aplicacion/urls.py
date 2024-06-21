from django.urls import path
from .views import ObtenerDatosApi

urlpatterns = [
    path('obtener-datos/', ObtenerDatosApi.as_view(), name='obtener-datos'),
]