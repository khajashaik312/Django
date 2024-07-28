from django import forms
from myapp.models import signup

class SignUpForm(forms.ModelForm):
	class Meta:
		model=signup
		fields=['username','password','email']