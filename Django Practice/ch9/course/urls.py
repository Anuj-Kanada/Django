from django.urls import path
from .views import py_course

urlpatterns = [
    path('python', py_course)
]