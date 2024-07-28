from django.shortcuts import render

# Create your views here.
def view1(request):
    return render(request,'index.html')

def view2(request):
    return render(request,'index1.html')

def tel(request):
    return render(request,'telugu.html')

def hin(request):
    return render(request,'hindi.html')