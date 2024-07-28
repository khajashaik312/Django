from django.shortcuts import render

# Create your views here.
def my_view(request):
	myName="shreenath"
	favPlayer="Dhoni"
	favAnimal="Lion"
	favSubject="python"
	d={"name":myName,"player":favPlayer,"animal":favAnimal,"subject":favSubject}
	return render(request,"myapp/1.html",d)