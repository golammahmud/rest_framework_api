from django.contrib import admin
from django.urls import path,include
from fapi.views import EmployeeApi

urlpatterns = [
    # path('functionapi/', function_api),
    # path('functionapi/<int:pk>', function_api),
    path('functionapi/', EmployeeApi.as_view()),
    path('functionapi/<int:pk>', EmployeeApi.as_view()),
]

