from django.shortcuts import render
from django.http import HttpResponse

'''def Home(request, name):
    return render(request, "index.html", {
        "name": name.capitalize() # context - dictionary with keys as variable names
    }) # by default searches for the specified html file in templates folder'''

def Home(request):
    return render(request, "index.html")

def defaulthellotest(request):
    return HttpResponse("Hello World")