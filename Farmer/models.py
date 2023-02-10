from django.db import models

class FarmerData(models.Model):
    uname = models.CharField(max_length = 10)
    fname = models.CharField(max_length = 30)
    lname = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    address = models.CharField(max_length = 100)
    phone_no = models.CharField(max_length = 11)
    place = models.CharField(max_length = 20, default = "HYD")
    seller = models.BooleanField(default = False)


class SellerData(models.Model):
    uname = models.CharField(max_length=10,default='none')
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 100)
    phone_no = models.CharField(max_length = 11)
    products = models.CharField(max_length = 50,default = 'none')
