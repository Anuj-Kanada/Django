from django.urls import path
from .views import myapp2

urlpatterns = [
    
    path('app2/', myapp2)
]