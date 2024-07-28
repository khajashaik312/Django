from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
	a=int(input("Enter the 1st value"))
	b=int(input("Enter the 2nd value"))
	print(a/b)
	print("Inside View Function")
	return HttpResponse("<h1>Successfully landed on the page</h1>")