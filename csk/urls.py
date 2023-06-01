from django.urls import path
from csk.views import *
app_name='shinchan'

urlpatterns=[

    path('dhoni/',dhoni,name='dhoni')
]