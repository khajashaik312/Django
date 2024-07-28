from django import forms
from django.core import validators
class FeedBackForm(forms.Form):
	name=forms.CharField()
	rollno=forms.IntegerField()
	email=forms.EmailField()
	feedback=forms.CharField(widget=forms.Textarea)
	def clean(self):
		print("one clean mtd for all validators")
		data=super().clean()
		n=data['name']
		if n[0].lower()!='s':
			raise forms.ValidationError("name must start with s or S")
		r=data['rollno']
		if r<=0:
			raise forms.ValidationError("rollno must be +ve")