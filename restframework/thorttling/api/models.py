from django.db import models



class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    city=models.CharField(max_length=100)
    def __str__(self):
        return self.name

#for all eisting users token generate
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
#
# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)
