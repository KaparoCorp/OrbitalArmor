from django.contrib import admin
from .models import NetworkTraffic, UploadedPcap

# Register your models here.
admin.site.register(NetworkTraffic)
admin.site.register(UploadedPcap)