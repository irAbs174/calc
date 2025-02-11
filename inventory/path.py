from django.urls import path
from .views import *

urlpatterns = [
    path('create_new', create_new),
    path('list', inventory_list),
]