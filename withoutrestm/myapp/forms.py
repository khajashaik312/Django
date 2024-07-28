from django import forms
from myapp.models import Employee
class EmployeeForm(forms.ModelForm):
	def clean_esal(self):
		sal=self.cleaned_data['esal']
		if sal<15000:
			raise forms.ValidationError("sal cannot be<15000")
			return sal
	class Meta:
		model=Employee
		fields="__all__"