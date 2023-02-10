from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    #path("<str:name>", views.Home, name='Home'),
    path("", views.labindex, name='LabIndex'),
    path("Register/",views.register, name='register'),
    path("Login/",views.Login, name="Login"),
    path("Login/bookings/",views.bookings, name="bookings")
]
urlpatterns += staticfiles_urlpatterns()