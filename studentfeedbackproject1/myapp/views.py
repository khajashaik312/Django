from django.shortcuts import render
from myapp.forms import FeedBackForm
# Create your views here.
def feedbackView(request):
	f=FeedBackForm()
	if request.method=="POST":
		f=FeedBackForm(request.POST)
		if f.is_valid():
			name=f.cleaned_data['name']
			rollno=f.cleaned_data['rollno']
			email=f.cleaned_data['email']
			feedbak=f.cleaned_data['feedback']
			d={'name':name,'rollno':rollno,'email':email,'feedback':feedbak}
			return render(request,'myapp/output.html',d)
	d={'form':f}
	return render(request,'myapp/feedback.html',d)