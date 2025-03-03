from django.urls import path
from .views import learn_django

urlpatterns = [
    
    path('py/', learn_django)
]