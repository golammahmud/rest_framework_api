from rest_framework import serializers
from .models import Studentapi

class StudentSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=100)
    class Meta:
        model = Studentapi
        fields = ['id','name','roll','city']