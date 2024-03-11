from django.shortcuts import render
from django.views.generic import View, TemplateView
from django_pandas.io import read_frame
from dashboard.models import NetworkTraffic
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from registration.models import CustomUser
import os
from django.contrib.auth import logout

import psutil  # for info on network interface

#global variables
user = CustomUser.objects.all()

# Create your views here.

class Dashboard(View):
    #template for dashboard landing page view 
    template_name = "dashboard.html"
      #Retrieve all NetworkTraffic data saved
    queryset = NetworkTraffic.objects.all()
    
    #convert the querySet to a panas Dataframe
    networkTraffic_df = read_frame(queryset)
    networkTraffic_df = networkTraffic_df
    data = networkTraffic_df.dropna()
    y = data.label
    label = ['Malicious', 'Bengin']

    def get(self, request):
        x = dict(self.data.label.value_counts())[0]
        y = dict(self.data.label.value_counts())[1]
        sizes = [x,y]
        context = {
        "label":self.label,
        }
        context['sizes']= sizes
        fig = px.pie(data_frame=None, values=sizes, labels=self.label, title="Malicious to Bengin Traffic")
        fig = fig.to_html()
        context['fig'] = fig
        return render(request, self.template_name, context)

class Alarm(View):
    # template for  alarm view for alerts and notification of ddos
    template_name = "alarm.html"

    #data retrival form data base 
    queryset = NetworkTraffic.objects.all()

    #manipulate data 
    networkTraffic_df = read_frame(queryset)
    networkTraffic_df = networkTraffic_df.dropna()
    data = networkTraffic_df
    y = data.label
    
    def get(self, request):
        context = {}
        #ip graph data and bar graph
        x = list(dict(self.data[self.data.label == 1].src.value_counts()).keys())
        y = list(dict(self.data[self.data.label == 1].src.value_counts()).values())
        data = [x, y]
        fig = px.bar(data_frame=None,x = x, y = y, title="Number of requests",labels={"x":"Ip address of senders", "y": " Number of requests"})
        fig = fig.to_html()
        context['fig'] = fig

        #protocols data and bar graph
        protocolName = list(dict(self.data.Protocol.value_counts()).keys())
        protocolsValues = list(dict(self.data.Protocol.value_counts()).values())
        protocolsMaliciousName = list(dict(self.data[self.data.label == 1].Protocol.value_counts()).keys())
        protocolsMaliciousValue = dict(self.data[self.data.label == 1].Protocol.value_counts()).values()
        figProtocol = px.bar(data_frame=None, x=protocolName, y = protocolsValues, title="Protocols ", labels={"x": "Protocol Name", "y": " Request count"})
        figProtocol = figProtocol.to_html()
        context['figProtocol'] = figProtocol

        #duration data and bar graph
        durationInfo = self.data.dur
        durationHist = px.line(data_frame=None, x=durationInfo, title="Duration histogram", labels={"x":"Duration in seconds", "y":"count in Bytes"})
        durationHist = durationHist.to_html()
        context['durationHist'] = durationHist

        #transmission data and histogram
        transmissionInfo = self.data.tx_bytes
        transmissionHist = px.histogram(data_frame=None, x = transmissionInfo, title="Transmittion Bytes histogram", labels={"x":"Duration in seconds","y":"count in Bytes"})
        transmissionHist = transmissionHist.to_html()
        context["transmissionHist"] = transmissionHist 
        
        #kbps data and histogram graph
        kbpsInfo = self.data.tx_kbps
        kbpsHist = px.histogram(data_frame=None, x = kbpsInfo, title="Rate trassmitted in Kbps", labels={"x":"Duration in seconds ", "y":"count in kbp"})
        kbpsHist = kbpsHist.to_html()
        context['kbpsHist'] = kbpsHist

        return render(request, self.template_name, context)


#view for user page...contain data of user and ability to log out
#Username, operating system, company name, position in company, network interfaces, ip address,
#log out button
class UserAuthPage(View):
    # template for users view for user data and logout
    template_name = "user.html"
    def get(self, request):
        #get content for page
        #get os name
        context = {}
        osName = os.uname().sysname
        context['os'] = osName

       #get network interfaces
        interfaces = psutil.net_if_addrs()
        networkInterfaces = list(psutil.net_if_addrs())
        context['NIC'] = networkInterfaces
        
        #get ip address from NIC info
        IP = networkInterfaces
        IP= IP
        context['IP'] = IP
        loger=logout(request)
        context['logout'] = loger
        return render(request, self.template_name, context)