from django.db import models

class LabTable(models.Model):
    labid = models.CharField(max_length = 10)
    labname = models.CharField(max_length = 30)
    place = models.CharField(max_length = 30)
    address = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 11, default = '9505486964')
    email = models.CharField(max_length = 30, default= 'abc@gmail.com')
    password = models.CharField(max_length = 30,default = 'namehere')

class Bookings(models.Model):
    labid = models.CharField(max_length = 10)
    cusname = models.CharField(max_length = 60, default="Ramu")
    bookingdate = models.DateField()
    phone = models.CharField(max_length = 11)
    address = models.TextField(max_length = 100)
