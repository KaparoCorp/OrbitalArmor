from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('history', views.Historty.as_view(), name='history'),
    path('signIn/', views.SignIn , name='signIn'),
    
]