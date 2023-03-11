from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your models here.

class ObservableModel(models.Model):
    observers = []
    
    class Meta:
        abstract = True
    
    def add_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
    
    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
    
    def notify_observers(self, **kwargs):
        for observer in self.observers:
            observer.update(self, **kwargs)


class Donor(ObservableModel):
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
    
class WelcomeEmailObserver:
    def update(self, observable, **kwargs):
        if isinstance(observable, Donor) and kwargs.get('created', False):
            user = observable
            
            send_mail(
                'Welcome to My Site',
                f'Hi {user.donor_first_name},\n\nThanks for joining My Site!',
                'lifesourcebloodbankadm@gmail.com',
                [user.user.email],
                fail_silently=False,
            )