from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import StudentSerializer
from .models import  Students
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


from  rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend




# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer
#     lookup_field = 'slug'
  
  
  
  

# modelviewset 
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    filter_backends=[SearchFilter,DjangoFilterBackend,OrderingFilter]
    filterset_fields=['name','roll']
    search_fields=['$name','=roll','=classes']
    ordering_fields=['name','roll','classes']
    
    lookup_field = 'slug'







    
# class StudentViewSet(viewsets.ViewSet):
#     lookup_field = 'slug'
#     def list(self,request):
#         stu=Students.objects.all()
#         serializer=StudentSerializer(stu,many=True)
#         return Response(serializer.data)
    
#     def retrieve(self,request,slug=None):
#         slug=slug
#         if slug is not None:
#             stu=Students.objects.get(slug=slug)
#             serializers=StudentSerializer(stu)
#             return Response(serializers.data )
#         stu=Students.objects.all()
#         serializers=StudentSerializer(stu,many=True)
#         return Response(serializers.data,status=status.HTTP_200_OK)
    
#     def create(self,request,slug=None):
#         serializer=StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message":"data insert succefully"},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors ,status=status.HTTP_204_NO_CONTENT)
    
#     def update(self,request,slug=None):
#         slug=slug
#         stu=Students.objects.get(slug=slug)
#         serializer=StudentSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message":"data update succefully"},status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors ,status=status.HTTP_204_NO_CONTENT)
    
#     def partial_update(self,request,slug=None):
#         slug=slug
#         stu=Students.objects.get(slug=slug)
#         serializer=StudentSerializer(stu,data=request.data ,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message":"partially data updated succefully"},status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    
  
#     def destroy(self,request,slug=None):
#         slug=slug
#         stu=Students.objects.get(slug=slug)
#         if stu is None:       
#             stu.delete()
#             return Response({'message':'data was successfully deleted'},status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_204_NO_CONTENT)
  
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
#class based apiview
# class StudentViewSet(APIView):
#     def get(self,request,pk=None,formate=None):
#         id=pk
#         if id is not None:
#             stu=Students.objects.get(id=id)
#             serializers=StudentSerializer(stu)
#             return Response(serializers.data )
#         stu=Students.objects.all()
#         serializers=StudentSerializer(stu,many=True)
#         return Response(serializers.data)
#     def post(self,request,pk=None,formate=None):
#         serializer=StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message":"data insert succefully"},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    
#     def put(self,request,pk=None,formate=None):
#         id=pk
#         stu=Students.objects.get(pk=id)
#         serializer=StudentSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message":"data update succefully"},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    
#     def patch(self,request,pk=None,formate=None):
#         id=pk
#         stu=Students.objects.get(pk=id)
#         serializer=StudentSerializer(stu,data=request.data ,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message":"partially data updated succefully"},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    
 