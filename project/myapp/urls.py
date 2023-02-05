from django.contrib import admin
from django.urls import path, include 
from myapp import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('contactus/', views.contactus, name = 'contactus'),

]