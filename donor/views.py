from django.shortcuts import render


def donation_history_view(request):
        return render(request,'donor/Donationhistory.html')


def login(request):
        return render(request, 'donor/pages-login.html')


def donor_signup_view(request):
        return render(request,'donor/pages-register.html')


def questionnare_view(request):
        return render(request, 'donor/questionnaire.html')


def questionnairefail_view(request):
        return render(request,'donor/questionnairefail.html')


def users_profile_view(request):
        return render(request, 'donor/users-profile.html')
