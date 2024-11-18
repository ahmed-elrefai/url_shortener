from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('urls/create/',create_url ,name='create_url'),
    path('<str:short>/',resolve_url ,name='resolve_url'),
]