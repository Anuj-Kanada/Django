from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def learn_django(req):
    return HttpResponse("WElcome to The App1")