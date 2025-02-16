"""cbvproject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path as url
from myapp.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',EmployeeView.as_view(),name="employeelist"),
    url(r'^(?P<pk>\d+)/',EmployeeDetailView.as_view(),name="employeedetail"),
    url(r'^create/',EmployeeCreateView.as_view(),name="create"),
    url(r'^update/(?P<pk>\d+)',EmployeeUpdateView.as_view(),name="update"),
    url(r'^delete/(?P<pk>\d+)',EmployeeDeleteView.as_view(),name="delete")
]