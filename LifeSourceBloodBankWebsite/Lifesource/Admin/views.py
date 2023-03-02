from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Events
from django.contrib import messages
from .import forms, models
 


@login_required(login_url='login')
def admin_submit_data(request):
    return render(request, 'admin_submit_data.html')

@login_required(login_url='login')
def admin_edit_appt(request):
    return render(request, 'admin_edit_appt.html')

@login_required(login_url='login')
def admin_update_appt(request):
    return render(request, 'admin_update_appt.html')
  
@login_required(login_url='login')
def admin_create_apptPage(request):
    data = Events.objects.all()
    print(data)
    context = {"data": data}
    return render(request, 'admin_create_appt.html', context)

 

def insertData(request):
    if request.method == "POST":
        ename = request.POST.get('ename')
        apptname = request.POST.get('apptname')
        elocation = request.POST.get('elocation')
        eaddress = request.POST.get('eaddress')
        epscode = request.POST.get('epscode')
        edate = request.POST.get('edate')
        etimest = request.POST.get('etimest')
        etimend = request.POST.get('etimend')
        print(ename, elocation, edate, etimest, etimest)
        query = Events(ename=ename, apptname=apptname, elocation=elocation, eaddress=eaddress,
                       epscode=epscode, edate=edate, etimest=etimest, etimend=etimend)
        query.save()
        messages.info(request, "Data Inserted Successfully")
        return redirect("admin_create_appt")
    admin_create_apptPage()


@login_required(login_url='login')
def updateData(request, id):
    if request.method == "POST":
        ename = request.POST['ename']
        apptname = request.POST['apptname']
        elocation = request.POST['elocation']
        eaddress = request.POST['eaddress']
        epscode = request.POST['epscode']
        edate = request.POST.get('edate')
        etimest = request.POST.get('etimest')
        etimend = request.POST.get('etimend')
        edit = Events.objects.get(id=id)
        edit.ename = ename
        edit.apptname = apptname
        edit.elocation = elocation
        edit.eaddress = eaddress
        edit.epscode = epscode
        edit.edate = edate
        edit.etimest = etimest
        edit.etimend = etimend
        edit.save()
        messages.warning(request, "Data Updated Successfully")
        return redirect("admin_create_appt")
        admin_edit_appt()

    d = Events.objects.get(id=id)
    context = {"d": d}
    return render(request, "admin_edit_appt.html", context)


def deleteData(request, id):
    d = Events.objects.get(id=id)
    d.delete()
    messages.error(request, "Data deleted Successfully")
    return redirect("admin_create_appt")
    admin_create_apptPage()
 

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('admin_create_appt')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')
 