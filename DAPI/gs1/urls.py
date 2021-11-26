from django.contrib import admin
from django.urls import path,include
from .views import StudentApi

urlpatterns = [
    path('student/', StudentApi.as_view(),name='Student_info'),
]
