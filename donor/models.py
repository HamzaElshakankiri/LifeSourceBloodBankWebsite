from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Donor(models.Model):
    #donor_id=models.IntegerField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True, default=1,related_name="donor_profile")
    donor_first_name=models.CharField(max_length=25,blank=False,null=False)
    donor_last_name=models.CharField(max_length=25,blank=False,null=False)
    #donor_password=models.CharField(max_length=25)
    donor_postal=models.CharField(max_length=10)
    #donor_email=models.CharField(max_length=20,null=False)
    donor_bio_sex=models.CharField(max_length=25,blank=False,null=False)
    donor_blood_type=models.CharField(max_length=10)
    donor_birthday=models.DateField(null=True)
    donor_weight=models.PositiveIntegerField(default=0)
    donor_height=models.PositiveIntegerField(default=0)
    donor_contact_phone=models.CharField(max_length=25)
    emergency_contact_name=models.CharField(max_length=25)
    emergency_contact_phone=models.CharField(max_length=25)
    donor_nextdonationdate=models.DateField(auto_now=True)

    def __str__(self) :
        return self.user.email