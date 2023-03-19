from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect,reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . import forms,models
from .models import Donor, WelcomeUserEmailObserver, NewUserJoinedObserver
from Admin.models import Events
from datetime import date
from datetime import datetime

today = date.today()

#index Page View
def index(request):
    return render(request, 'index.html')

#Sign Up View
def donor_signup_view(request):  
        #Load Form   
        userForm=forms.DonorUserForm()
        donorForm=forms.DonorForm()
        mydict={'userForm':userForm,'donorForm':donorForm}
        if request.method=='POST':
                #Receive Form Info
                userForm=forms.DonorUserForm(request.POST)
                donorForm=forms.DonorForm(request.POST)
                #If Forms are Valid
                if userForm.is_valid() and donorForm.is_valid():
                     #Save Form   
                     user=userForm.save()
                     user.set_password(user.password)
                     user.save()
                     
                     donor=donorForm.save(commit=False)
                     donor.user=user
                     donor.donor_bio_sex=donorForm.cleaned_data['donor_bio_sex']
                     donor.save()
                     
                     #Add User to DB                     
                     my_donor_group = Group.objects.get_or_create(name='DONOR')
                     my_donor_group[0].user_set.add(user)
                     
                     #Email Observers
                     donor.add_observer(WelcomeUserEmailObserver())
                     donor.add_observer(NewUserJoinedObserver())
                     donor.notify_observers(created=True)
                     donor.remove_observer(WelcomeUserEmailObserver())
                     donor.remove_observer(NewUserJoinedObserver())
                     return HttpResponseRedirect(reverse('pages-login'))
                else:
                        #show Errors
                        print(userForm.errors)
                        print(donorForm.errors)
        return render(request,'pages-register.html',context=mydict)

#Users Profile
@login_required(login_url='pages-login')
def users_profile(request,donor_email):
        #Load Users data
        user = User.objects.filter(email=donor_email).first()
        donor = Donor.objects.filter(user__email=donor_email)
        
        #Fill In User Data
        print(donor)
        if donor.exists():
                donor = donor.first()
        # Access the donor_first_name attribute on the first donor in the queryset
                print(donor.donor_birthday)
        else:
                print('No donor found')
        context = { 'user' : user, 'donor' : donor}
        return render(request, 'users-profile.html',context)

#Edit users profile
@login_required(login_url='pages-login')
def updateProfile(request, donor_id):
        #Load Users Data
        user = User.objects.filter(id=donor_id).first()
        donor = Donor.objects.filter(user_id=donor_id).first()
        context = {}
        print(user)
        if request.method == "POST":
                #Shows User Data
                donor_first_name = request.POST['donor_first_name']
                donor_last_name = request.POST['donor_last_name']
                donor_bio_sex = request.POST['donor_bio_sex']
                donor_birthday = request.POST['donor_birthday']
                donor_blood_type = request.POST['donor_blood_type']
                donor_postal = request.POST['donor_postal']
                donor_contact_phone = request.POST['donor_contact_phone']
                donor_height = request.POST['donor_height']
                donor_weight = request.POST['donor_weight']
                emergency_contact_name = request.POST['emergency_contact_name']
                emergency_contact_phone = request.POST['emergency_contact_phone']

                donor_birthday_datetime = datetime.strptime(donor_birthday, '%Y-%m-%d')

                #updates Users Data
                edit = Donor.objects.filter(user_id=donor_id).first()
                edit.donor_first_name = donor_first_name
                edit.donor_last_name =  donor_last_name
                edit.donor_bio_sex = donor_bio_sex                        
                edit.donor_birthday = donor_birthday_datetime               
                edit.donor_blood_type = donor_blood_type
                edit.donor_postal = donor_postal                        
                edit.donor_contact_phone = donor_contact_phone
                edit.donor_height = donor_height
                edit.donor_weight = donor_weight
                edit.emergency_contact_name = emergency_contact_name
                edit.emergency_contact_phone = emergency_contact_phone
                edit.save()
                context = {'donor' : edit}
        
                messages.warning(request, "Data Updated Successfully")
        else:
           donor = Donor.objects.filter(user_id=donor_id).first()
           context = {'donor' : donor}
        return render (request,'users-profile.html',context)

#Booking Appointment
@login_required(login_url='pages-login')
def donor_bookappt(request):
    #Load Events    
    event = Events.objects.filter(edonor_email='0', edonor_name='').filter(edate__gte=today)
    context = { 'event' : event}
    return render(request, 'donor_bookappt.html', context)

#Booking Appointment Pre Questionnaire
@login_required(login_url='pages-login')
def donor_bookappNoQ(request):
    #Load Events     
    event = Events.objects.filter(edonor_email='0', edonor_name='').filter(edate__gte=today)
    context = { 'event' : event}
    return render(request, 'donor_bookappNoQ.html', context)

#Book Appointment per User
@login_required(login_url='pages-login')
def bookAppt(request,e_id,donor_email):
       #Loading events and User data
       event = Events.objects.get(id=e_id)
       event.edonor_email=donor_email
       donor = Donor.objects.get(user__email=donor_email)
       dName = donor.donor_first_name.strip() + " " + donor.donor_last_name.strip()
       dBlood = donor.donor_blood_type
       event.edonor_blood=dBlood
       event.edonor_name=dName
       event.save()       
       return redirect('Donation.history.html')

#Show Current Appoinments 
@login_required(login_url='pages-login')
def donor_currentappt_specific(request,donor_email):
    event = Events.objects.filter(edonor_email=donor_email).filter(edate__gte=today)
    context = { 'event' : event}
    return render(request, 'donor_currentappt.html', context)

#Show Current Appoinments Per User
@login_required(login_url='pages-login')
def donor_currentappt(request,e_id,donor_email):
        #Loading events and User data
        event = Events.objects.get(id=e_id)
        event.edonor_email=donor_email
        donor = Donor.objects.get(user__email=donor_email)
        dName = donor.donor_first_name.strip() + " " + donor.donor_last_name.strip()
        event.edonor_name=dName
        dBlood = donor.donor_blood_type
        event.edonor_blood=dBlood
        event.save()
        context = {}
        event = Events.objects.filter(edonor_email=donor_email).filter(edate__gte=today)
        print(event)
        context = {'donor_email':donor_email,'event' : event}
        return render(request,'donor_currentappt.html',context)

#User Cancelling Appointment
@login_required(login_url='pages-login')
def donor_delete_currentappt(request,e_id,donor_email):
        #Removing the appointment
        event = Events.objects.get(id=e_id)
        event.edonor_email='0'
        event.edonor_name=''
        event.save()
        context = {}
        event = Events.objects.filter(edonor_email=donor_email).filter(edate__gte=today)
        print(event)
        context = {'donor_email':donor_email,'event' : event}
        return render(request,'donor_currentappt.html',context)

#Showing User Donation History
@login_required(login_url='pages-login')
def donation_history_view(request,donor_email):
        event = Events.objects.filter(edonor_email=donor_email).filter(edate__lt=today)
        context = { 'event' : event}
        return render(request,'Donationhistory.html',context)
 
#Questionnaire     
@login_required(login_url='pages-login')           
def questionnare_view(request):
        return render(request, 'questionnaire.html')

#Questionnaire Fail 
@login_required(login_url='pages-login')
def questionnairefail_view(request):
        return render(request,'questionnairefail.html')

#User Profile  
@login_required(login_url='pages-login')
def users_profile_view(request):
        return render(request, 'users-profile.html')

#Log Out
def LogoutPage(request):
    logout(request)
    return redirect('index')


"""def donor_login_view(request):
        if request.method=='POST':
                username=request.POST.get('username')
                password=request.POST.get('password')
                user=authenticate(request,username=username,password=password)
                print('USER: ',user)
                if user is not None:
                        login(request,user)
                        return redirect('donation-history')
                else:
                        return HttpResponse ("Username or Password is incorrect!")

        return render(request, 'pages-login.html')"""