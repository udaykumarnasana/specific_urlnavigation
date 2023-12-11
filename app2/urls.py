from django.urls import path
from app2.views import *

app_name='responce'

urlpatterns=[
    path('hr/',hr,name='hr'),
]