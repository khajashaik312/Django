from django.contrib import admin
from myapp.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
	l=['eid','ename','esal','edesig','eexp']
admin.site.register(Employee,EmployeeAdmin)