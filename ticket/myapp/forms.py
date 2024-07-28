from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import *
        
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['BoardingPoint','DestinationPoint','NoofPassengers','PassengerName','PassengerAge','Gender','ServiceCategory','DepartOn','ArrivalOn','Category','SeatNo']
    