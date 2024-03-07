from django.db import models
from registration.models import CustomUser


#["dt", "switch", "src", "dst", "pktcount", "bytecount", "dur", "dur_nsec"]
#["tot_dur", "flows", "packetins", "pktperflow", "byteperflow", "pktrate"]
#["Pairflow", "Protocol", "port_no,tx_bytes", "rx_bytes", "tx_kbps", "rx_kbps,tot_kbps", "label]
#stringdata["Protocol", "dst", "src"]


# Create your models here.
class NetworkTraffic(models.Model):
    dt = models.IntegerField(name='dt')
    switch = models.IntegerField(name='switch')
    src = models.GenericIPAddressField(name="src", protocol='IPv4')
    dst = models.GenericIPAddressField( name = "dst", protocol="IPv4")
    pktcount = models.IntegerField(name='pktcount')
    bytecount = models.IntegerField(name='bytecount')
    dur = models.IntegerField(name='dur')
    dur_nsec = models.IntegerField(name='dur_nsec')
    tot_dur = models.IntegerField(name='tot_dur')
    flows = models.IntegerField(name='flows')
    packetins = models.IntegerField(name='packetins')
    pktperflow = models.IntegerField(name='pktperflow')
    byteperflow = models.IntegerField(name='byteperflow')
    pktrate = models.IntegerField(name='pktrate')
    Pairflow = models.IntegerField(name='Pairflow')
    Protocol = models.CharField(name="Protocol", max_length=5)
    port_no = models.IntegerField(name='port_no')
    tx_bytes = models.IntegerField(name='tx_bytes')
    rx_bytes = models.IntegerField(name='rx_bytes')
    tx_kbps = models.IntegerField(name='tx_kbps')
    rx_kbps = models.IntegerField(name='rx_kbps')
    tot_kbps = models.IntegerField(name='tot_kbps')
    label = models.IntegerField(name='label')