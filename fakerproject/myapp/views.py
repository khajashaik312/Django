from django.shortcuts import render
from myapp.models import Student
from django.db.models import Count
def fakerView(request):
	s=Student.objects.exclude(marks__range=(40,50))
	d={'stud':s}
	return render(request,'myapp/output.html',d)