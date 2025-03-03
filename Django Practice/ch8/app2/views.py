from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def myapp2(req):
    return HttpResponse('<h1>Welcome to myapp2')
