from django.shortcuts import render
from django.http import HttpResponse
from Farmer.models import SellerData

def fromfarmindex(request): 
    f = SellerData.objects.all()
    return render(request, 'fromfarmindex.html',{'sellerlist':f})
