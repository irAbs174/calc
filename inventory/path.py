from django.urls import path
from .views import *

urlpatterns = [
    path('create_new', create_new),
    path('list', inventory_list),
    path('category_list', category_list),
    path('create_new_category', create_new_category),
    path('manager_list', manager_list),
    path('add_manager', add_manager),
]