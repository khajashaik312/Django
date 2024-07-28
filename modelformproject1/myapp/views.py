from django.shortcuts import render
from myapp.models import Student
from myapp.forms import StudentForm
# Create your views here.
def input_View(request):
    f=StudentForm()
    if request.method=="POST":
        f=StudentForm(request.POST)
        if f.is_valid():
            f.save(commit=True)
            #to save the changes we commit=True
            return render(request,'myapp/1.html',{'form':f})
def output_View(request):
    s=Student.objects.all()
    d={'stud':s}
    return render(request,'myapp/2.html',d)