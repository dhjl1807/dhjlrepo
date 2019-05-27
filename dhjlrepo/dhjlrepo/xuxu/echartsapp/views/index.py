from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_view(request):
    print(request.path)
    return HttpResponse('<h2>Hello</h2>')