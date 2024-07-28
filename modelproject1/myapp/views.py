from django.shortcuts import render
from myapp.models import Employee
# Create your views here.
def EmployeeView(request):
	e=Employee.objects.all()
	d={'emp':e}
	return render(request,'myapp/1.html',d)