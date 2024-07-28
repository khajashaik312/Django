from django.shortcuts import render

# Create your views here.
def template_view(request):
    name="dhoni"
    id=101
    place="blore"
    context={'key1':name,'key2':id,'key3':place}
    return render(request,'myapp/1.html',context)