from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import  Students


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Students
        fields = ['id', 'name','slug', 'roll','classes']
        # fields='__all__'
        # include=['id']
        # read_only_fields=['roll']
        # extra_kwargs ={'name':{'write_only':True}}
        
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

    def validate_roll(self,value):
        if value>200:
            raise serializers.ValidationError('roll is must be between 200')
        if Students.objects.filter(roll=value).exists():
            raise serializers.ValidationError('roll already exists')            
        return value

