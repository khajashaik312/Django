from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
    s="<h1>this is 1st response"
    return HttpResponse(s)

def view2(request):
    s1=int(input("Enter 1st num:"))
    s2=int(input("Enter 2nd num:"))
    s3=s1+s2
    return HttpResponse(str(s3))

