from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
	s="Inside myapp1"
	return HttpResponse(s)