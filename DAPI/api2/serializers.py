from rest_framework import serializers
from api2.models import Employee

# validators
def start_with_p(value):
    if value[0].lower() != 'p':
        raise serializers.ValidationError('Name shuld be start with p')

class StudentSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=100,read_only=True,validators=[start_with_p])#for specific object validations
    class Meta:
        model = Employee
        fields = ['id','name','email','phone','city']
        #exclude = ['roll']
        # fields='__all__'
        #read_only_fields=['name','email',]#for read only mulitiple field validations
        # extra_kwargs={'name':{'read_only':True,'required':'True'},}
        # field level validations
    def validate_roll(self, value):
        if value >= 100:
            raise serializers.ValidationError('seat full')
        return value

        # object level validations

    def validate(self, data):
        if data['name'] == 'parvez' and data['city'] != 'pabna':
            raise serializers.ValidationError("name should be pabna")
        return data


