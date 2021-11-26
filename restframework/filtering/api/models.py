from django.db import models
from django.contrib.auth.models import User



class Student(models.Model):
    name=models.CharField(max_length=100,default='')
    roll=models.IntegerField(default='')
    city=models.CharField(max_length=100,default='')
    passby=models.ForeignKey(User,default='',on_delete=models.CASCADE)
    def __str__(self):
        return self.name

#for all eisting users token generate
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
#
# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)
