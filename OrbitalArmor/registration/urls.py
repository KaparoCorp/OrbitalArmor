from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutUs.as_view(), name='about'),
    path('history/', views.History.as_view(), name='history'),
    path('signIn/', views.SignIn.as_view() , name='signIn'),
    path('register/', views.Registration.as_view(), name='signUp'),
    
]