from django.urls import path
from .views import *

urlpatterns = [
    path('personal_list', personal_list),
    path('add_personal', add_personal),
    path('create_department', create_department),
    path('department_list', department_list),
]