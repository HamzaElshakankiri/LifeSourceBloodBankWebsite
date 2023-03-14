from django.db import models
from datetime import date

# Create your models here.

class Stock(models.Model):
    bloodgroup = models.CharField(max_length=10)
    unit = models.IntegerField(default=0)

    def __str__(self):
        return self.bloodgroup

class Events(models.Model):
    ename = models.CharField(max_length=25, blank=False, null=False)
    eaddress = models.CharField(max_length=25, blank=False, null=False)
    epscode = models.CharField(max_length=25, blank=False, null=False)
    edate = models.CharField(max_length=25, blank=False, null=False)
    etimest = models.CharField(max_length=25, blank=False, null=False)
    etimend = models.CharField(max_length=25, blank=False, null=False)
    edonor_email = models.CharField(max_length=25, default='0')
    edonor_name = models.CharField(max_length=50, default='')
    edonor_blood = models.CharField(max_length=10, default='Unknown')
    event_type = models.CharField(max_length=25,blank=False,null=False,default='')

    def __str__(self):
        return self.ename