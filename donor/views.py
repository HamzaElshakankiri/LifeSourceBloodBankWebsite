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

def index(request):
    return render(request, 'index.html')

def donor_bookappt(request):
    return render(request, 'donor_bookappt.html')

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
def donation_history_view(request):
        user = request.user
        donor = Donor.objects.get(user=user)
        donor_first_name= donor.donor_first_name
        context={'donor_first_name':donor_first_name}
        return render(request,'Donationhistory.html')
     
           
def questionnare_view(request):
        return render(request, 'questionnaire.html')


def questionnairefail_view(request):
        return render(request,'questionnairefail.html')


def users_profile_view(request):
        return render(request, 'users-profile.html')
