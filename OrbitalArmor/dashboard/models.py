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


class UploadedPcap(models.Model):
    user = models.ForeignKey("registration.CustomUser", verbose_name=("username"), on_delete=models.CASCADE)
    src_ip = models.CharField( name = "src_ip",max_length=10)
    dst_ip = models.CharField( name = "dst_ip",max_length=10)
    src_port = models.IntegerField(name='src_port')
    dst_port = models.IntegerField(name='dst_port')
    protocol = models.IntegerField(name="protocol")
    flowsbytes = models.IntegerField(name='flowsbytes')
    flow_pkts_s = models.IntegerField(name='flow_pkts_s')
    active_max = models.IntegerField(name='active_max')
    idle_max = models.IntegerField(name='idle_max')
    down_up_ratio = models.IntegerField(name='down_up_ratio')
    pkt_size_avg = models.IntegerField(name='pkt_size_avg')
    pkt_len_max = models.IntegerField(name='pkt_len_max')
    fwd_pkt_len_max = models.IntegerField(name='fwd_pkt_len_max')
    bwd_pkt_len_max = models.IntegerField(name='bwd_pkt_len_max')
    tot_fwd_pkts = models.IntegerField(name='tot_fwd_pkts')
    tot_bwd_pkts = models.IntegerField(name='tot_bwd_pkts')
    totlen_fwd_pkts = models.IntegerField(name='totlen_fwd_pkts')
    totlen_bwd_pkts = models.IntegerField(name='totlen_bwd_pkts')
    Label = models.CharField(name='Label', max_length=10)