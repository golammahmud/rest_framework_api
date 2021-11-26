from django.contrib import admin
from django.urls import path,include
from api2.views import StudentApi

urlpatterns = [
    path('employee/', StudentApi.as_view(),name='Student_info'),
]
