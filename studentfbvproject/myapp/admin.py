from django.contrib import admin
from myapp.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
	l=['ename','eno','esal','eaddr']
admin.site.register(Employee,EmployeeAdmin)