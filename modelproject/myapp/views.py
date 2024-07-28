from django.shortcuts import render
from myapp.models import Student
# Create your views here.
def myview(request):
	s=Student.objects.all()
	print(type(s))
	d={'stud':s}
	return render(request,'myapp/1.html',d)