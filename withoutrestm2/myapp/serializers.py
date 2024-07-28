from rest_framework import serializers
class EmployeeSerializer(serializers.serializer):
	eno=serializers.IntegerField()
	ename=serializers.CharField(max_length=60)
	esal=serializers.FloatField()
	eaddr=serializers.CharField(max_length=100)