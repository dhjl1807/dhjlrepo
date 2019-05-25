from django.urls import path

from echartsapp.views import *

app_name = 'echartsapp'

urlpatterns = [
    path('index/',index_view),
    path('dili/',dili_view),
    path('ciyun/',ciyun_view),
]