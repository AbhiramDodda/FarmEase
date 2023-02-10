from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import SignUpForm, LoginForm, LabBookForm, SellerRegForm
import sqlite3
from Farmer.models import FarmerData, SellerData
from Laboratory.models import LabTable, Bookings
from datetime import date
import requests, json

l = []
def index(request):
    form = LoginForm(request.POST)
    return render(request, 'farmerindex.html', {'form':form})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            if request.POST["password"] == request.POST["repassword"]:
                fname = request.POST['fname']
                lname = request.POST['lname']
                phone = request.POST['phoneno']
                address = request.POST['address']
                place = request.POST['place']
                password = request.POST['password']
                uname = generateuname(fname,phone,lname)
                f = FarmerData(uname=uname, fname = fname, lname = lname, phone_no = phone,address =  address,password = password, place = place) 
                f.save()
                return render(request, 'userHome.html',{'fname':fname, 'uname':uname,'temperature':gettemp(),'weather_disc':getdisc()})
        else:
            return render(request, 'farmerRegister.html')
    form = SignUpForm()
    return render(request, 'farmerRegister.html', {'form': form})
    

def generateuname(a,b,c):
    return a[:3] + b[3:7] + c[-1]  

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            farmers = FarmerData.objects.all()
            check = False
            for farmer in farmers:
                print(farmer.password, farmer.uname)
                if farmer.uname == request.POST['username'] and farmer.password == request.POST['pwd']:
                    check = True
                    l.append(farmer.uname)
                    name = farmer.fname + ' ' + farmer.lname
                    l.append(name)
                    l.append(farmer.place)
                    l.append(farmer.address)
                    return render(request, 'userHome.html', {'fname' : farmer.fname,'temperature':gettemp(),'weather_disc':getdisc(),'uname':farmer.uname})   
            if not check:
                return render(request, 'farmerindex.html',{'form': form})
        return render(request, 'farmerindex.html',{'form':form})
    form = LoginForm()
    return render(request, 'farmerindex.html', {'form': form})

def showlabs(request):
    labs = LabTable.objects.all()
    form = LabBookForm(request.POST)
    return render(request, 'showlabs.html',{'labs':labs, 'form':form})

def booktest(request):
    bookings = Bookings.objects.all()
    labs = LabTable.objects.all()
    if request.method == 'POST':
        form = LabBookForm(request.POST)
        if form.is_valid():
            rf=""
            uid = request.POST['uid']
            lib = request.POST['labid']
            farmers = FarmerData.objects.all()
            check = False
            for farmer in farmers:
                if farmer.uname == uid:
                    check = True
                    rf = farmer
                    break
            if not check:
                return render(request, 'showlabs.html',{'form' : form,'labs':labs})
            today = date.today()
            f = Bookings(cusname=rf.fname+' '+rf.lname,bookingdate = today, phone = rf.phone_no,address = rf.address,labid = lib)
            f.save()
            mybookings=[]
            mylab = ""
            ch = False
            for booking in bookings:
                if booking.cusname == rf.fname+' '+rf.lname and booking.phone == rf.phone_no:
                    mybookings.append(booking)
            if len(mybookings) == 0:
                ch = True
            for lab in labs:
                if lib == lab.labid:
                    mylab = lab
                    break
            print(mybookings)
            print(mylab)
            return render(request, 'showlabs.html', {'form': form, 'bookings': mybookings, 'mylab': mylab, 'labs':labs})
        return render(request, 'showlabs.html',{'form':form})
    form = LabBookForm()
    return render(request, 'showlabs.html',{'form':form})

    
    
def seller(request):
    if request.method == 'POST':
        form = SellerRegForm(request.POST)
        if form.is_valid():
            farmers = FarmerData.objects.all()
            myfarmer = ''
            check = False
            for farmer in farmers:
                if farmer.uname == request.POST['uname']:
                    myfarmer = farmer
                    check = True
                    break
            if not check:
                return render(request, 'sellerregistration.html',{'form':form})
            fname = myfarmer.fname
            lname = myfarmer.lname
            address = myfarmer.address
            name = fname + ' ' + lname
            f = SellerData(uname = myfarmer.uname,name = name,address = myfarmer.address, phone_no = myfarmer.phone_no,products = request.POST['products'])
            f.save()
            product_list = request.POST['products'].split(',')
            return render(request, 'registeredseller.html',{'fname':myfarmer.fname, 'lname': myfarmer.lname,'productlist':product_list})
        return render(request, 'sellerregistration.html',{'form':form})
    form = SellerRegForm()
    return render(request, 'sellerregistration.html',{'form':form})

def gettemp():
    api_key = "4cb61764d0b9a1bfeafecf02f0931359"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + "Hyderabad"
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
    else:
        print(" City Not Found ")
    return current_temperature - 273.13

def getdisc():
    api_key = "4cb61764d0b9a1bfeafecf02f0931359"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + "Hyderabad"
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
    else:
        print(" City Not Found ")
    return weather_description

def profile(request):
    return render(request, 'profile.html',{'uname':l[0],'name':l[1],'place':l[2],'address':l[3]})



    