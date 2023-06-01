from django.urls import path
from rcb.views import *
app_name='nobitha'

urlpatterns=[
    path('virat/',virat,name='virat'),
]