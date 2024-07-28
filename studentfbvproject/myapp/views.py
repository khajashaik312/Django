#redirect()==>used to redirect the control flow to read a particular page/==>Home page
from django.shortcuts import render,redirect
from myapp.models import Employee
from myapp.forms import EmployeeForm
# Create your views here.
def display(request):
	e=Employee.objects.all()
	d={'emp',e}
	return render(request,'myapp/index.html',d)

def insert_view(request):
	f=EmployeeForm()
	if request.method=="POST":
		f=EmployeeForm(request.POST)
		if f.is_valid():
			f.save(commit=True)
		return redirect('/')
	d={'form':f}
	return render(request,'myapp/insert.html',d)

def delete_view(request,id): #deletion of a particular record with id
	e=Employee.objects.get(id=id)
	e.delete()
	return redirect('/')

def update_view(request,id):
	e=Employee.objects.get(id=id)
	if request.method=="POST":
		e=EmployeeForm(request.POST,instance=e)
		if e.is_valid():
			e.save(commit=True)
			return redirect('/')
	d={'emp':e}
	return render(request, 'myapp/update.html',d)