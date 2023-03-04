from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *


def donation_history_view(request):
        return render(request,'donor/Donationhistory.html')


def donor_login_view(request):
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

        return render(request, 'donor/pages-login.html')


def donor_signup_view(request):
        return render(request,'donor/pages-register.html')


def questionnare_view(request):
        return render(request, 'donor/questionnaire.html')


def questionnairefail_view(request):
        return render(request,'donor/questionnairefail.html')


def users_profile_view(request):
        return render(request, 'donor/users-profile.html')
