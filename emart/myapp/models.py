from django.db import models


# Create your models here.
class Emart(models.Model):
    DCGST_NO=models.CharField( max_length=15)
    DBILL_NO=models.CharField( max_length=15)
    PURCHASE_DT=models.DateTimeField( auto_now=False, auto_now_add=False)
    DEALER_NAME=models.CharField( max_length=50)
    PHONE_NUMBER=models.CharField(max_length=13)
    PRODUCT_NAME=models.CharField( max_length=50)
    TNOP=models.DecimalField( max_digits=10, decimal_places=0)
    PPP=models.DecimalField( max_digits=10, decimal_places=2)
    TC=models.DecimalField( max_digits=10, decimal_places=2)
    

class Bill(models.Model):
    Emart_GST_NO=models.CharField( max_length=15, default="141FA08121FA081")
    DATE_TIME=models.DateTimeField( auto_now=False, auto_now_add=False, null=True)
    BILL_NO=models.IntegerField()
    CUSTOMER_NAME=models.CharField( max_length=50)
    MOBILE_NO=models.CharField(max_length=50)
    PRODUCT_LIST=models.CharField( max_length=50)
    PRODUCT_PRICE=models.DecimalField( max_digits=10, decimal_places=2)