from django.contrib import admin
from .models import Studentapi

@admin.register(Studentapi)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','roll','city']
