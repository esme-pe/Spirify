#importaciones:
from django.urls import path
from home.views import home_inicio

ulrlpatterns = [
    path('', home_inicio)
]