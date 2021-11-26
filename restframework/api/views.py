from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,DjangoModelPermissions
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser,IsAuthenticated]

from rest_framework.authtoken.models import Token

# token = Token.objects.create(user=instance)
# print(token.key)
