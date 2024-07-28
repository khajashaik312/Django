from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def bill(request):
    context={}
    context['billform']=BillForm()
    if request.method=="POST":
        data=BillForm(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse('Bill saved successfully. . .')
    return render(request,"bill.html",context)

def emart(request):
    context={}
    context['emartform']=EmartForm()
    if request.method=="POST":
        data=EmartForm(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse('Dealer form created successfully')
    return render(request,"emart.html",context)
    

def emart2(request):
    context={}
    cur=connection.cursor()
    cur.execute('select * from sys.myapp_emart')
    data=cur.fetchall()
    context={'detailes':data}
    return render(request,'emart2.html',context)