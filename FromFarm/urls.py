from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    #path("<str:name>", views.Home, name='Home'),
    path("", views.fromfarmindex, name='Home')
]
urlpatterns += staticfiles_urlpatterns()