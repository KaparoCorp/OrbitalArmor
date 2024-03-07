from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('alarm/', views.Alarm.as_view(), name='alarm'),
    path('user/', views.UserAuthPage.as_view(), name="user"),
    
]