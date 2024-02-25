from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    
]