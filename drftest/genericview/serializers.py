from django.contrib.auth.models import User, Group
from genericview.models import Course
from rest_framework import serializers
# from .models import  Students


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model =Course
        fields = '__all__'
        include=['url']
        # read_only_fields=['roll']
        lookup_fields ='slug'
        extra_kwargs ={'url':{'lookup_fields':'slug'}}
    

    # def validate_roll(self,value):
    #     if value>200:
    #         raise serializers.ValidationError('roll is must be between 200')
    #     # if Students.objects.filter(roll=value).exists():
    #         raise serializers.ValidationError('roll already exists')            
    #     return value

