from django.urls import path
from . import views
#Urls.py file specifically for this app, will be connected to overall project in urls.py in mysite directory
urlpatterns = [
    path('', views.index,name='index') #/my_apps -> PROJECT urls.py
]