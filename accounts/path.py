from django.urls import path
from .auth import login

urlpatterns = [
    path('login', login),
]