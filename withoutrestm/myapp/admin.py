from django.contrib import admin
from myapp.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
	l=['id','eno','ename','esal','eaddr']
admin.site.register(Employee,EmployeeAdmin)