from django.urls import path
from myapp import api
from myapp.views import *

app_name = 'myapp'

urlpatterns = [
    path(r'home/', go_home, name='home'),
    path(r'qksou/', quicksou, name='qksou'),
    path(r'regist/', regist, name='regist'),
    path(r'login/', login_view, name='login'),
    path(r'code/', api.get_code),
    path(r'jobs/', to_jobs, name='jobs'),
    path(r'logout/', logout, name='logout'),
    path(r'company/<name>/', to_company, name='company'),
    path(r'job/<name>/<pagenum>/', find_jobs, name='job')
]

