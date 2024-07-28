from django.contrib import admin
from myapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	l=['number','name','marks']
admin.site.register(Student,StudentAdmin)
