from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api.views import StudentViewSet
router=DefaultRouter()
from rest_framework import urls
from rest_framework.authtoken.views import obtain_auth_token

router.register('studentapi',StudentViewSet ,basename='studentapi')

urlpatterns = [


    path('', include(router.urls)),
    path('api/auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
