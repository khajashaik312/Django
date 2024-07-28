from django.shortcuts import render
from myapp.models import Employee
from django.http import HttpResponse
from django.views.generic import View
from myapp.mixins import SerializeMixin,HttpResponseMixin
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from myapp.utils import is_json
from myapp.forms import EmployeeForm 

@method_decorator(csrf_exempt,name="dispatch")
class EmployeeDetails(SerializeMixin,HttpResponseMixin,View):
    def get(self,request,id,*args,**kwargs):
        try:
            emp=Employee.objects.get(id=id)
        except:
            json_data=json.dumps({'msg':'The requested resource is unavailable'})
            return self.render_to_http_response(json_data,status=404)
        else:
            json_data=self.fun([emp])
            return self.render_to_httpResponse(json_data)
    def get_object_by_id(self,id):
        try:
            emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp=None
            return emp

    def put(self,request,id,*args,**kwargs):
        emp=self.get_object_by_id(id=id)
        if emp is None:
            json_data=json.dumps({'msg':'No Such Record'})
            return self.render_to_http_response(json_data,status=404)
            data=request.body
            valid=is_json(data)
            if not valid:
                json_data=json.dumps({'msg':'invalid data form'})
                return self.render_to_http_response(json_data,status=404)
                provided_data=json.loads(data)

        original_data={'eno':emp.eno,'ename':emp.ename,'esal':emp.esal,'eaddr':emp.eaddr}
        original_data.update(provided_data)
        form=EmployeeForm(original_data,instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Resource has been updated successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data=json.dumps({'msg':'Form contains errors'})
            return self.render_to_http_response(json_data)

    def delete(self,request,id,*args,**kwargs):
        emp=self.get_object_by_id(id=id)
        if emp is None:
            json_data=json.dumps({'msg':'No Such Record'})
            return self.render_to_http_response(json_data,status=404)
            t=emp.delete()
            print(t)

@method_decorator(csrf_exempt,name="dispatch")
class EmployeeList(SerializeMixin,HttpResponseMixin,View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        json_data=self.fun(qs)
        return HttpResponse(json_data,content_type='application/json')
    def post(self,request,*args,**kwargs):
        data=request.body
        valid=is_json(data)
        if not valid:
            json_data=json.dumps({'msg':'invalid data form'})
            return self.render_to_http_response(json_data,status=404)
            emp_data=json.loads(data)
            form=EmployeeForm(emp_data)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Resource has been created successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data=json.dumps({'msg':'Form contains errors'})
            return self.render_to_http_response(json_data)