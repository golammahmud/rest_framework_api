from django.shortcuts import render

from fapi.serializers import EmployeeSerializer
from api2.models import Employee
from rest_framework import viewsets

class modelview(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
