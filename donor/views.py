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
from .models import Donor
from Admin.models import Events
from datetime import date

today = date.today()

def index(request):
    return render(request, 'index.html')


def donor_signup_view(request):
        
        userForm=forms.DonorUserForm()
        donorForm=forms.DonorForm()
        mydict={'userForm':userForm,'donorForm':donorForm}
        if request.method=='POST':
                userForm=forms.DonorUserForm(request.POST)
                donorForm=forms.DonorForm(request.POST)

                if userForm.is_valid() and donorForm.is_valid():
                     user=userForm.save()
                     user.set_password(user.password)
                     user.save()
                     
                     donor=donorForm.save(commit=False)
                     donor.user=user
                     donor.donor_bio_sex=donorForm.cleaned_data['donor_bio_sex']
                     donor.save()
                     my_donor_group = Group.objects.get_or_create(name='DONOR')
                     my_donor_group[0].user_set.add(user)
                     return HttpResponseRedirect(reverse('pages-login'))
                else:
                        print(userForm.errors)
                        print(donorForm.errors)
        return render(request,'pages-register.html',context=mydict)

@login_required(login_url='pages-login')
def users_profile(request,donor_email):
        user = User.objects.filter(email=donor_email).first()
        donor = Donor.objects.filter(user__email=donor_email)
        
        print(donor)
        if donor.exists():
                donor = donor.first()
        # Access the donor_first_name attribute on the first donor in the queryset
                print(donor.donor_birthday)
        else:
                print('No donor found')
        context = { 'user' : user, 'donor' : donor}
        return render(request, 'users-profile.html',context)






@login_required(login_url='pages-login')
def donor_bookappt(request):
    event = Events.objects.filter(edonor_email='0').filter(edate__gte=today)
    context = { 'event' : event}
    return render(request, 'donor_bookappt.html', context)

@login_required(login_url='pages-login')
def bookAppt(request,e_id,donor_email):
       event = Events.objects.get(id=e_id)
       event.edonor_email=donor_email
       event.save()
       
       return redirect('Donation.history.html')

@login_required(login_url='pages-login')
def donor_currentappt_specific(request,donor_email):
    event = Events.objects.filter(edonor_email=donor_email).filter(edate__gte=today)
    context = { 'event' : event}
    return render(request, 'donor_currentappt.html', context)

       

@login_required(login_url='pages-login')
def donor_currentappt(request,e_id,donor_email):
        event = Events.objects.get(id=e_id)
        event.edonor_email=donor_email
        event.save()
        context = {}
        event = Events.objects.filter(edonor_email=donor_email).filter(edate__gte=today)
        print(event)
        context = {'donor_email':donor_email,'event' : event}
        return render(request,'donor_currentappt.html',context)

@login_required(login_url='pages-login')
def donor_delete_currentappt(request,e_id,donor_email):
        event = Events.objects.get(id=e_id)
        event.edonor_email='0'
        event.save()
        context = {}
        event = Events.objects.filter(edonor_email=donor_email).filter(edate__gte=today)
        print(event)
        context = {'donor_email':donor_email,'event' : event}
        return render(request,'donor_currentappt.html',context)


@login_required(login_url='pages-login')
def donation_history_view(request,donor_email):
        event = Events.objects.filter(edonor_email=donor_email).filter(edate__lt=today)
        context = { 'event' : event}
        return render(request,'Donationhistory.html',context)
     
           
def questionnare_view(request):
        return render(request, 'questionnaire.html')


def questionnairefail_view(request):
        return render(request,'questionnairefail.html')




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