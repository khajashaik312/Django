from django import forms
from myapp.models import Student
class StudentForm(forms.ModelForm):
	class Meta:#contains model,fields
		model=Student
		fields='__all__'
		#fields=('f1','f2','f3','f4')
		#exclude=('f2','f3')