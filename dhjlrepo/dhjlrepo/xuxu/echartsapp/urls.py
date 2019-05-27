from django.urls import path

from echartsapp.views import *
from echartsapp.views.wordcloud import create_wordcloud

app_name = 'echartsapp'

urlpatterns = [
    path('index/', index_view),
    path('dili/', dili_view),
    path('ciyun/', ciyun_view),
    path('citysalary/', citysalary_view),
    path('citysalary/<city>/', citysalary_view),
    path('edusalary/', edusalary_view),
    path('edusalary/<edu>/', edusalary_view),
    path('yearsalary/', yearsalary_view),
    path('yearsalary/<city>/', yearsalary_view),
    path('wordcloud/<table_name>/', create_wordcloud),
]
