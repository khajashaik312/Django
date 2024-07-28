from django.db import models

# Create your models here.
class Dmart(models.Model):
    DCGST_NO=models.CharField( max_length=15)
    DBILL_NO=models.CharField( max_length=15)
    PURCHASE_DT=models.DateTimeField( auto_now=False, auto_now_add=False)
    DEALER_NAME=models.CharField( max_length=50)
    PHONE_NUMBER=models.CharField(max_length=13)
    PRODUCT_NAME=models.CharField( max_length=50)
    TNOP=models.IntegerField()
    PPP=models.DecimalField( max_digits=20, decimal_places=10)
    TC=models.DecimalField( max_digits=30, decimal_places=20)
