from django.contrib import admin
from myapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	l=['name','number','marks','place']
admin.site.register(Student,StudentAdmin)