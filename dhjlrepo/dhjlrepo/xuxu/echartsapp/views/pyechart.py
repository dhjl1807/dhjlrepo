from django.http import HttpResponse
from echartsapp.echarts import *


def dili_view(request):
    html = dilifenbutu().render_embed()
    return HttpResponse(html)


def ciyun_view(request):
    html = bossciyun().render_embed()
    return HttpResponse(html)


def citysalary_view(request, city='西安'):
    html = citysalary(city).render_embed()
    return HttpResponse(html)


def edusalary_view(request, edu='本科'):
    html = edusalary(edu).render_embed()
    return HttpResponse(html)


def yearsalary_view(request, city='西安'):
    html = yearsalary(city).render_embed()
    return HttpResponse(html)
