from django.contrib import admin
from genericview.models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=('title','slug','credits')
# Register your models here.
