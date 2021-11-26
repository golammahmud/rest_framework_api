from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,DjangoModelPermissions
from .models import Student
from .serializers import StudentSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


from rest_framework.views import APIView
from rest_framework.response import Response

class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


























































# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)

from rest_framework.authtoken.models import Token

# token = Token.objects.create(user=instance)
# print(token.key)


#signals for instance user token
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
#
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)