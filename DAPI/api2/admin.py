from django.contrib import admin
from api2.models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone','city']

