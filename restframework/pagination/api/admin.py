from django.contrib import admin

from .models import Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city','passby']

# from rest_framework.authtoken.models import Token
# admin.site.register(Token)
