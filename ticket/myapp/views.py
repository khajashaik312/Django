from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from.models import *
from .forms import *


# Create your views here.
def bill(request):
    context={}
    context['ticketform']=TicketForm()
    if request.method=='POST':
        data=TicketForm(request.POST)
        if data.is_valid():
            data.save()
            return render(request,'ticket.html')
    return render(request,'bill.html',context)


def bill2(request):
    context={}
    if request.method=='POST':
        psgname=request.POST['psgname1']
        cur=connection.cursor()
        cur.execute('select * from practice.myapp_ticket where PassengerName=%s',(psgname,))
        data=cur.fetchall()
        context={'detailes':data}
    return render(request,'bill2.html',context)

def printticket(request):
    return render(request,'ticket.html')