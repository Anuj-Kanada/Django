from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_django(req, **kwargs):
    status = kwargs.get('status','Not Allowed')
    print(status)
    return HttpResponse(f'<h1>Welcome to Django {status} - App1 </h1>')

