from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
    s="<h1>This is 1st Response"
    return HttpResponse(s)

def view2(request):
    s="<h1>This is 2nd Response"
    return HttpResponse(s)