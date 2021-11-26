from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
