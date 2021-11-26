from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework import viewsets
from .models import Studentapi


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Studentapi.objects.all()
    serializer_class = StudentSerializer


