from django import forms
from .models import *

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields="__all__"

class EmartForm(forms.ModelForm):
    class Meta:
        model = Emart
        fields="__all__"