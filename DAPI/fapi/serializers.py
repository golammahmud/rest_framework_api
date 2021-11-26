from rest_framework import serializers
from api2.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=100)
    class Meta:
        model = Employee
        fields = ['id','name','email','phone','city']