from django.db import models

# Create your models here.
class Ticket(models.Model):
    boarding=(('Rajahmundry','Rajahmundry'),('Vijayawada','Vijayawada'),('Visakhapatnam','Visakhapatnam'),('Hyderabad','Hyderabad'),('Jangareddygudem','Jangareddygudem'))
    destination=(('Rajahmundry','Rajahmundry'),('Vijayawada','Vijayawada'),('Visakhapatnam','Visakhapatnam'),('Hyderabad','Hyderabad'),('Jangareddygudem','Jangareddygudem'))
    service=(('SUPER LUXURY','SUPER LUXURY'),('SUPER DELUXE','SUPER DELUXE'))
    gender=(('Male','Male'),('Female','Female'))
    status=(('CONFIRMED','CONFIRMED'),('PENDING','PENDING'))
    #DepartTime=(('20.30P.M','20.30P.M'),('21.00P.M','21.00P.M'),('22.00P.M','22.00P.M'),('23.00P.M','23.00P.M'))
    #ArrivalTime=(('06.00A.M','06.00A.M'),('07.30A.M','07.30A.M'),('08.00A.M','08.00A.M'),('09.00A.M','09.00A.M'))
    #pickup=(('',''))
    #droping=(('',''))
    category=(('ADULT','ADULT'),('CHILD','CHILD'))
    seatno=(('01 w','01 w'),('02','02'),('03 w','03 w'),('04 w','04 w'),('05','05'),('06','06'),('07 w','07 w'),
            ('08 w','08 w'),('09','09'),('10','10'),('11 w','11 w'),('12 w','12 w'),('13','13'),('14','14'),
            ('15 w','15 w'),('16 w','16 w'),('17','17'),('18','18'),('19 w','19 w'),('20 w','20 w'),('21','21'),
            ('22','22'),('23 w','23 w'),('24 w','24 w'),('25','25'),('26','26'),('27 w','27 w'),('28 w','28 w'),
            ('29','29'),('30','30'),('31 w','31 w'),('32 w','32 w'),('33','33'),('34','34'),('35','35'),
            ('36 w','36 w'),)
    
    BoardingPoint=models.CharField(max_length=100,choices=boarding,default='Rajahmundry')
    DestinationPoint=models.CharField(max_length=100,choices=destination,default='Hyderabad')
    NoofPassengers=models.IntegerField()
    PassengerName=models.CharField(max_length=100)
    PassengerAge=models.IntegerField()
    Category=models.CharField(choices=category,max_length=50,null=True)
    Gender=models.CharField(choices=gender,max_length=100)
    ServiceCategory=models.CharField(choices=service,max_length=50,null=True)
    DepartOn=models.DateField(auto_now=False, auto_now_add=False,null=True)
    ArrivalOn=models.DateField(auto_now=False, auto_now_add=False,null=True)
    Status=models.CharField(choices=status,max_length=50)
    SeatNo=models.CharField(choices=seatno,max_length=50,null=True)  

    def __str__(self):
        return self.PassengerName