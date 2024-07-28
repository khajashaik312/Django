from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.bill),
    path('bill2',views.bill2),
    path('print',views.printticket)
]
