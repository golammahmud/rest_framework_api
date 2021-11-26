from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api.views import StudentViewSet
router=DefaultRouter()
from rest_framework import urls
from rest_framework.authtoken.views import obtain_auth_token
from .customtoken import CustomAuthToken

router.register('studentapi',StudentViewSet ,basename='studentapi'),


urlpatterns = [

    path('', include(router.urls)),
    path('api/auth/', include('rest_framework.urls')),
    # path('api-token-auth/', obtain_auth_token),
    path('api-token-auth/', CustomAuthToken.as_view())
]
# http  http://127.0.0.1:8000/api-token-auth/ 'Authorization: Token 24837218e57a052335c9cd344b58e9bd53f11bd6'
# http  http://127.0.0.1:8000/studentapi/ 'Authorization: Token 24837218e57a052335c9cd344b58e9bd53f11bd6'
#


