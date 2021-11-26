from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api.views import StudentViewSet
from  .views import HelloView
router=DefaultRouter()
from rest_framework import urls
from rest_framework.authtoken.views import obtain_auth_token

router.register('studentapi',StudentViewSet ,basename='studentapi'),


urlpatterns = [


    path('hello/',HelloView.as_view() ),
    path('', include(router.urls)),
    path('api/auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
]
# http post http://127.0.0.1:8000/api-token-auth/ username="user1" password="testing321"
#


