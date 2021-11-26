from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from modelviewapi.views import modelview


router=DefaultRouter()
router.register('eapi',modelview,basename='eapi')


urlpatterns = [
path('',include('router.urls')),
]

