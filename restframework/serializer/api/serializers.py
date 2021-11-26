from rest_framework import serializers
from rest_framework import viewsets
from .models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Student
        fields=('url','id','name','roll','city')


