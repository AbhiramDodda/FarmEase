from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import SignUpForm, LoginForm
import sqlite3
from Laboratory.models import LabTable, Bookings


def labindex(request):
    form = LoginForm(request.POST)
    return render(request, 'labindex.html', {'form':form})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            if request.POST["password"] == request.POST["repassword"]:
                labname = request.POST['labname']
                email = request.POST['email']
                phone = request.POST['phone']
                address = request.POST['address']
                place = request.POST['place']
                password = request.POST['password']
                labid = generateuname(labname,phone)
                f = LabTable(labid = labid,labname=labname, phone = phone,address =  address,password = password, place = place,email = email) 
                f.save()
                return render(request, 'userHome.html',{'labname':labname, 'uname':labid})
        else:
            return render(request, 'Register.html')
    form = SignUpForm()
    return render(request, 'Register.html', {'form': form})
    

def generateuname(a,b):
    return a[:3] + b[3:7]  

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            labs = LabTable.objects.all()
            check = False
            for lab in labs:
                print(lab.password, lab.labid)
                if lab.labid == request.POST['username'] and lab.password == request.POST['pwd']:
                    check = True
                    return render(request, 'labuserHome.html',{'labname':lab.labname})   
            if not check:
                return render(request, 'labindex.html',{'form': form})
        return render(request, 'lab.html')
    form = LoginForm()
    return render(request, 'labindex.html', {'form': form})

def bookings(request):
    labbookings = Bookings.objects.all()
    mybookings = []
    for booking in labbookings:
        if booking.labid == "Ram5486":
            mybookings.append(booking)
    print(mybookings)
    return render(request, 'bookings.html',{'bookingslist':mybookings})

    
    
