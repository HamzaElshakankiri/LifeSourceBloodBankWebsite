from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Events
from django.contrib import messages
from .import forms, models
from .models import Stock
from django.db.models import Sum, Q 


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
 
def home_view():
    blood1 = Stock()
    blood1.bloodgroup = "A+"
    blood1.save()

    blood2 = Stock()
    blood2.bloodgroup = "A-"
    blood2.save()

    blood3 = Stock()
    blood3.bloodgroup = "B+"
    blood3.save()

    blood4 = Stock()
    blood4.bloodgroup = "B-"
    blood4.save()

    blood5 = Stock()
    blood5.bloodgroup = "AB+"
    blood5.save()

    blood6 = Stock()
    blood6.bloodgroup = "AB-"
    blood6.save()

    blood7 = Stock()
    blood7.bloodgroup = "O+"
    blood7.save()

    blood8 = Stock()
    blood8.bloodgroup = "O-"
    blood8.save()


@login_required(login_url='login')
def AdminDash(request):
    x = Stock.objects.all()
    if len(x) == 0:
        home_view()
    totalunit = Stock.objects.aggregate(Sum('unit'))
    a = Stock.objects.get(bloodgroup="A+")
    a1 = Stock.objects.get(bloodgroup="A-")
    b = Stock.objects.get(bloodgroup="B+")
    b1 = Stock.objects.get(bloodgroup="B-")
    ab = Stock.objects.get(bloodgroup="AB+")
    ab1 = Stock.objects.get(bloodgroup="AB-")
    o = Stock.objects.get(bloodgroup="O+")
    o1 = Stock.objects.get(bloodgroup="O-")
    context = {
        'a': a,
        'a1': a1,
        'b': b,
        'b1': b1,
        'ab': ab,
        'ab1': ab1,
        'o': o,
        'o1': o1,
        'totalbloodunit': totalunit['unit__sum'],
    }
    return render(request, 'admin_dashboard.html', context)


@login_required(login_url='login')
def AdminDonation(request):
    data = Events.objects.all()
    print(data)
    context = {"data": data}
    return render(request, 'admin_donation.html', context)


@login_required(login_url='login')
def admin_blood(request):
    a = Stock.objects.get(bloodgroup="A+")
    a1 = Stock.objects.get(bloodgroup="A-")
    b = Stock.objects.get(bloodgroup="B+")
    b1 = Stock.objects.get(bloodgroup="B-")
    ab = Stock.objects.get(bloodgroup="AB+")
    ab1 = Stock.objects.get(bloodgroup="AB-")
    o = Stock.objects.get(bloodgroup="O+")
    o1 = Stock.objects.get(bloodgroup="O-")

    if request.method == 'POST':
        bloodForm = forms.BloodForm(request.POST)
        if bloodForm.is_valid():
            bloodgroup = bloodForm.cleaned_data['bloodgroup']
            unit = bloodForm.cleaned_data['unit']
            stock = Stock.objects.get(bloodgroup=bloodgroup)
            updated_unit = stock.unit + unit
            stock.unit = max(updated_unit, 0)
            stock.save()
        return redirect('admin_blood')

    else:
        bloodForm = forms.BloodForm()

    context = {
        'bloodForm': bloodForm,
        'a': a,
        'a1': a1,
        'b': b,
        'b1': b1,
        'ab': ab,
        'ab1': ab1,
        'o': o,
        'o1': o1,
    }

    return render(request, 'admin_blood.html', context=context)

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')
 