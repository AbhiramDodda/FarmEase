from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.index, name='index'),
    path("Register/", views.register, name = 'register'),
    path("Farmer/",views.login, name = 'login'),
    path('Login/', views.login,name = 'farmerlogin'),
    path("Login/showlabs/", views.showlabs, name='showlabs'),
    path("Login/sellerportal/", views.seller, name='sellerregister'),
    path("Login/showlabs/booktest/", views.booktest, name='testbooking'),
    path('Login/sellerportal/seller/', views.seller, name='registeredseller'),
    path('Login/profile/', views.profile, name='farmerprofile')
]

urlpatterns += staticfiles_urlpatterns()