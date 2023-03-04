from django.db import models

# Create your models here.

class Donor(models.Model):
    donor_id=models.IntegerField(primary_key=True)
    donor_name=models.CharField(max_length=25,blank=False,null=False)
    donor_password=models.CharField(max_length=25)
    donor_postal=models.CharField(max_length=10)
    donor_email=models.EmailField()
    donor_bio_sex=models.CharField(max_length=25,blank=False,null=False)
    donor_blood_type=models.CharField(max_length=10)
    donor_birthday=models.DateField(auto_now=True)
    donor_weight=models.PositiveIntegerField(default=0)
    donor_height=models.PositiveIntegerField(default=0)
    donor_contact_phone=models.CharField(max_length=25)
    emergency_contact_name=models.CharField(max_length=25)
    emergency_contact_phone=models.CharField(max_length=25)

    def __str__(self) :
        return self.donor_name