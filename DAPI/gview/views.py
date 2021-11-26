from django.shortcuts import render
from rest_framework.generics import GenericAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.response import Response
from fapi.serializers import EmployeeSerializer
from api2.models import Employee
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin

            #generic view
# class EmployeeApi(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
#
#
# class EmployeeApi_pk(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)


#concreate view
class EmployeeApi(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeApi_pk(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
