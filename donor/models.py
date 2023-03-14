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
    donor_contact_phone=models.PositiveIntegerField()
    emergency_contact_name=models.CharField(max_length=25)
    emergency_contact_phone=models.PositiveIntegerField()
    donor_nextdonationdate=models.DateField(auto_now=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self) :
        return self.user.email
    
class WelcomeUserEmailObserver:
    def update(self, observable, **kwargs):
        if isinstance(observable, Donor) and kwargs.get('created', False):
            user = observable
            
            send_mail(
                f'Welcome to Life Source Blood Bank!',
                f'Hi {user.donor_first_name} \nWelcome to Life Source Blood Bank! \nLife Source Blood Bank is a website made by Hamza Elshakankiri, Vishwa Gandhi, Sana Karedia, Jordan Seitz, and Marseel Yadkoo. This is a our project for CS 476, taught by Dr. Samira Sadaoui, at the University of Regina. \n\nOn our website, you can book appointments for any of the donation events available. You can also track the history of your past donations on our website. \nIf you have any questions, please contact us through our email, “LifeSourceBloodBankadm@gmail.com”. \nThank you, and we hope to improve your donation experience. \n\nSincerely, \nLife Source Blood Bank',
                'lifesourcebloodbankadm@gmail.com',
                [user.user.email],
                fail_silently=False,
            )

class NewUserJoinedObserver:
    def update(self, observable, **kwargs):
        if isinstance(observable, Donor) and kwargs.get('created', False):
            user = observable
            admin = 'lifesourcebloodbankadm@gmail.com'
            send_mail(
                'A New Donor Registered!',
                f'Hi Admin \n {user.donor_first_name} has joined the ranks of your donors! \nSincerely, \n \nLife Source Blood Bank ',
                'lifesourcebloodbankadm@gmail.com',
                [admin],
                fail_silently=False,
            )