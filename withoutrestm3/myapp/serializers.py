from rest_framework import serializers
from myApp.models import Employee
class EmployeeSerializer(serializers.Serializer):
    def multiples_of_1000(value):
        print("validation by validator attribute")
        if value%1000!=0:
            raise Exception("Emp sal must be multiple of 1000")
    def create(self,validated_data):
        return Employee.objects.create(**validated_data)
        #validated data containes kye:value pairs
    def update(self,instance,validated_data):
        instance.eno=validated_data.get('eno',instance.eno)
        instance.ename=validated_data.get('ename',instance.ename)
        instance.esal=validated_data.get('esal',instance.esal)
        instance.eaddr=validated_data.get('eaddr',instance.eaddr)
        instance.save()
        return instance

    eno=serializers.IntegerField()
    ename=serializers.CharField(max_length=6)
    esal=serializers.FloatField(validators=[multiples_of_1000])
    eaddr=serializers.CharField(max_length=100)