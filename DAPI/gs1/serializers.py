from rest_framework import serializers
from .models import Student


# validators
def start_with_p(value):
    if value[0].lower() != 'p':
        raise serializers.ValidationError('Name shuld be start with p')


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200, validators=[start_with_p])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=150)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    # field level validations
    def validate_roll(self, value):
        if value >= 100:
            raise serializers.ValidationError('seat full')
        return value

        # object level validations

    def validate(self, data):
        if data['name']=='parvez' and  data['city'] !='pabna':
            raise serializers.ValidationError("name should be pabna")
        return data


# def validate(self, attrs):
#     options = attrs.get('options')
#     item = attrs.get('item')
#
#
# if item not in options:
#     raise serializers.ValidationError('Item is not a valid option!')
