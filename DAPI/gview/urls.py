from django.contrib import admin
from django.urls import path,include
from gview.views import EmployeeApi,EmployeeApi_pk

urlpatterns = [
    path('generic/',EmployeeApi.as_view()),
    path('generic/<int:pk>',EmployeeApi_pk.as_view())
]

