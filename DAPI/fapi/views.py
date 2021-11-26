from django.shortcuts import render

from api2.models import Employee
from fapi.serializers import EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# @api_view(['GET', 'POST','PUT','PATCH','DELETE'])
# def function_api(request,pk=None):
#     if request.method == "GET":
#         # id=request.data.get('id')
#         if pk is not None:
#             stu=Employee.objects.get(id=pk)
#             serializer=EmployeeSerializer(stu)
#             return Response(serializer.data)
#         stu=Employee.objects.all()
#         serializer = EmployeeSerializer(stu,many=True)
#         return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == "POST":
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'data created'},status=status.HTTP_200_OK)
#
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == "PUT":
#         id=request.data.get('id')#for get app id
#         stu = Employee.objects.get(id=id)
#         # stu=Employee.objects.get(id=pk)#for get pk from url
#         serializer=EmployeeSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response('complete updated')
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == "PATCH":
#         # id=request.data.get('id')#for get app id
#         # stu = Employee.objects.get(id=id)
#         stu=Employee.objects.get(id=pk)#for get pk from url
#         serializer=EmployeeSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response('partial updated',status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == "DELETE":
#         # id=request.data.get('id')#for get app id
#         # stu = Employee.objects.get(id=id)
#         stu = Employee.objects.get(id=pk)  # for get pk from url
#         stu.delete()
#         return Response('data deleted',status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#class based view
from rest_framework.views import APIView

class EmployeeApi(APIView):
    def get(self,request,pk=None,formate=None):
        # id=request.data.get('id')
        if pk is not None:
            stu=Employee.objects.get(id=pk)
            serializer=EmployeeSerializer(stu)
            return Response(serializer.data)
        stu=Employee.objects.all()
        serializer = EmployeeSerializer(stu,many=True)
        return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def post(self, request, pk=None, formate=None):
        # id=request.data.get('id')


        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('data created',status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk=None,formate=None):
        # id =request.data.get('id')  # for get app id
        # stu = Employee.objects.get(id=id)
        stu = Employee.objects.get(id=pk)  # for get pk from url
        serializer = EmployeeSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('complete updated')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk=None,formate=None):
        # id =request.data.get('id')  # for get app id
        # stu = Employee.objects.get(id=id)
        stu = Employee.objects.get(id=pk)  # for get pk from url
        serializer = EmployeeSerializer(stu, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response('partial updated')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, formate=None):
        stu = Employee.objects.get(id=pk)  # for get pk from url
        stu.delete()
        return Response('data deleted',status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





