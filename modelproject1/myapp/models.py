from django.db import models
class Employee(models.Model):
		 eid=models.IntegerField()
		 ename=models.CharField(max_length=30)
		 edesig=models.CharField(max_length=40)
		 edob=models.DateField()
		 eexp=models.FloatField()
		 esal=models.IntegerField()
		 def __str__(self):
			  return self.ename
