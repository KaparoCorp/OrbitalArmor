#django default modules
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django_pandas.io import read_frame
from dashboard.models import NetworkTraffic
from django.contrib.auth import logout

#django models
from registration.models import CustomUser
from dashboard.models import UploadedPcap

#django forms
from dashboard.forms import UploadFileForm
from dashboard.handler import handle_uploaded_file

#other modules
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import os
from pathlib import Path
import psutil  # for info on network interface
 
#machine learning models
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler,  OneHotEncoder
from sklearn.compose import ColumnTransformer

# Create your views here.
#landing page view
class Dashboard(View):
    #template for dashboard landing page view 
    template_name = "dashboard.html"

    #get dashboard
    def get(self, request):
        context ={}
        return render(request, self.template_name, context)

# This is the Real Time data traffic
class Alarm(View):
    # template for  alarm view for alerts and notification of ddos
    template_name = "alarm.html"

    #data retrival form data base 
    queryset = NetworkTraffic.objects.all()

    #manipulate data 
    networkTraffic_df = read_frame(queryset)
    networkTraffic_df = networkTraffic_df.dropna()
    data = networkTraffic_df
    label = ['Malicious', 'Bengin']
    y = data.label
    
    def get(self, request):
        context = {}
        #malicous and bengin data
        x = dict(self.data.label.value_counts())[0]
        y = dict(self.data.label.value_counts())[1]
        sizes = [x,y]
        context = {
        "label":self.label,
        }
        context['sizes']= sizes
        fig = px.pie(data_frame=None, values=sizes, labels=self.label, title="Malicious to Bengin Traffic")
        chart = fig.to_html()
        context['chart'] = chart
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

        return render(request, self.template_name, context)

    def post(self, request):
        if request.POST:
            logout(request)
            return redirect('/')

#view for uploading files for machine to evaluate
#works with pcap and csv files
#uploaded files are in NetworkTraffic Folder and deleted after evaluation to save on space   
class UploadFile(View):
    teplate_name = "uploaded.html"
    #GET method
    def get(self, request):
        form = UploadFileForm()

        context = {"form" : form}


        return render(request, self.teplate_name, context)
    
    #POST method
    def post(self, request):
        context ={}
        #get file dataname
        if request.method == 'POST':
            file = request.FILES['networkFile'].name
            request.session['fileName'] = file
            
            handle_uploaded_file(request.FILES['networkFile'])
            return redirect('/results/')
        return render(request, self.teplate_name, context)


#viwe for showing results of uploaded file data after machine learning evaluation 
#uploaded file is evaluated using a presaved machine learning model
#results are in a pdf format for easy analysis and printing    
class Results(View):
    template_name = "results.html"
    def get(self, request):
        file = request.session['fileName'] #get filename uploaded
        context = {}
        user = CustomUser.objects.get(username=request.user)
        context['filename'] = file
        #use machine learning model on uploaded file
        with open('dashboard/Models/ml1.sav', 'rb') as machineFile:
            Model = joblib.load(machineFile) #machine model
            path = Path('NetworkTraffic')/Path(file) 
            data = pd.read_csv(path)
            data1 = data
            data1 = data1.drop(columns=["src_ip", "dst_ip","timestamp", "flow_duration", "src_port"])      
            X_pred = Model.predict(data1) #predicted label for uploaded file
            data = data.assign(Label = X_pred) #adding label column to dataset of uploaded file
            
            #save data of uploaded file to database
            for i in range(len(data)):
                traffic = UploadedPcap(
                    user=user,
                    src_ip= data.loc[i,'src_ip'],
                    dst_ip =data.loc[i,'dst_ip'],
                    src_port=data.loc[i,'src_port'], 
                    dst_port= data.loc[i,'dst_port'],
                    protocol= data.loc[i,'protocol'],
                    flowsbytes= data.loc[i,'flow_byts_s'], 
                    flow_pkts_s =data.loc[i,'flow_pkts_s'],
                    active_max = data.loc[i,'active_max'],
                    idle_max = data.loc[i,'idle_max'],
                    down_up_ratio= data.loc[i,'down_up_ratio'],
                    pkt_size_avg = data.loc[i,'pkt_size_avg'],
                    pkt_len_max = data.loc[i,'pkt_len_max'],
                    fwd_pkt_len_max = data.loc[i,'fwd_pkt_len_max'],
                    bwd_pkt_len_max = data.loc[i,'bwd_pkt_len_max'],
                    tot_fwd_pkts = data.loc[i,'tot_fwd_pkts'],
                    tot_bwd_pkts = data.loc[i,'tot_bwd_pkts'],
                    totlen_fwd_pkts = data.loc[i,'totlen_fwd_pkts'],
                    totlen_bwd_pkts = data.loc[i,'totlen_bwd_pkts'],
                    Label = data.loc[i,'Label'])
                traffic.save()

        #data retrival from database 
        queryset = UploadedPcap.objects.all()
        UploadedPcap_df = read_frame(queryset)
        UploadedPcap_df = UploadedPcap.dropna()
        data = UploadedPcap_df

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