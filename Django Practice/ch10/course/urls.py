from django.urls import path
from .views import learn_django, learn_fastapi

urlpatterns = [
    path('dj/',learn_django),
    path('fst/', learn_fastapi),
]
