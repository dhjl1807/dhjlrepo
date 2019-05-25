from django.http import HttpResponse
from echartsapp.echarts import *

def dili_view(request):
    html = dilifenbutu().render_embed()
    return HttpResponse(html)

def ciyun_view(request):
    html = bossciyun().render_embed()
    return HttpResponse(html)