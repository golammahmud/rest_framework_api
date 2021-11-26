from django.shortcuts import render
from rest_framework import generics 
from .models import Course
from .serializers import CourseSerializer

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin

# class CourseViewSet(RetrieveUpdateDestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#     lookup_field='slug'

# class CourseViewSet(ListModelMixin,GenericAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#     def get(self,request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# class CourseViewSet(CreateModelMixin,GenericAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#     def post(self,request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)





from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import permissions

from django_filters.rest_framework import DjangoFilterBackend
from  rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.validators import ValidationError

class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends=[SearchFilter,DjangoFilterBackend,OrderingFilter]
    filterset_fields=['title','credits']
    search_fields=['$title','=credits']
    ordering_fields=['title','credits']


            
          
                        
class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends=[SearchFilter,DjangoFilterBackend,OrderingFilter]
    filterset_fields=['title','credits']
    search_fields=['$title','=credits']
    ordering_fields=['title','credits']
    lookup_field='slug'
  
    


   