# This is a Project about DDOS ATTACK detection system using machine learning

## What is a denial of service attack?
DOS Attack--> Uses one internet connected device/network to flood the victims computer with malicious traffic so that when legitimate users are unable to access information systems, devices, or other network resources due to the actions of a malicious cyber threat actor.

Services affected may include email, websites, online accounts(Banking), or other services that rely on the affected computer or network. Can cost an organization both time and money while their resources and services are inaccessible.


DDOS --> Uses multiple internet connections to render the victims network inaccessible to them. DDos atackers often leverage the use of a botnet.DDos attacks have increased in magnitude as more and more devices come online through the Internet of Things(IoT)
IoT devices use default passwords and do not have sound security postures, making them vulnerable to compromise and exploitation.Infextion of IoT device often goes unnoticed by users, and an attacker could easily compromise hundreds of thousands of these devices to conduct a high-scale attack without the device owners' knowledge.


### Tools for DOS Attacks
1. Low Orbit Ion Cannon.
2. High Orbit Ion Cannon.
   
   

### Tools for DDOS Attacks
1. Botnet
2. Cloud Computing power in Botnets.
3. IoT.
   
### Methods
1. Application layer Attack
2. Volumetric Attack
3. Fragmentation Attack
4. Protocal Based Attack
   
## Installation Method
First thing is to make sure that your machine has all the requirments needed for the project and there found in the requirments.txt file.Requirements can be downloaded using python together with pip as follows :

``` python -m pip install -r requirements.txt ```

After installing requirements you will need to make database migrations for the data.``` python manage.py makemigrations ``` . Then ``` python manage.py migrate ```. Finally run the application by changing directory to OrbitalArmor and use ``` python manage.py runserver ```.

To access the web interface, head to your preffered browser and enter http://127.0.0.1:8000/ 

## How to use
The landing page is easy and interactive. The menu bar contains: 
1. The logo -> logo of the earth and name of system
2. About us -> about the developer and data.
3. History -> shows data about ddos attacks in the web and news
4. Sign up -> the registration page
5. Log in  -> the log in page
   
Afer a user is able to register an account and log in, the user is redirected to the dashboard page which is the heart of the system.


# System Design
For this project I have chosen to use python 3.10.12 and can be installed form their website python.org, pandas ,sciPy, NumPy,Matplotlib and skitlearn.


# Methods of ddos 

https://github.com/sammwyy/ddos-mitigation

Kernel Modifications
Drop ICMP ECHO-Requests
To prevent smurf attack.

echo 1 > /proc/sys/net/ipv4/icmp_echo_ignore_broadcasts
Dont accept ICMP Redirect
To prevent smurf attack.

echo 0 > /proc/sys/net/ipv4/conf/all/accept_redirects
Drop source routed packets
echo 0 > /proc/sys/net/ipv4/conf/all/accept_source_route
Enable SYN-Cookie for prevent SYN Flood
To prevent SYN Flood and TCP Starvation.

sysctl -w net/ipv4/tcp_syncookies=1
sysctl -w net/ipv4/tcp_timestamps=1
Increase TCP SYN backlog
To prevent TCP Starvation.

echo 2048 > /proc/sys/net/ipv4/tcp_max_syn_backlog
Decrease TCP SYN-ACK retries
To prevent TCP Starvation.

echo 3 > /proc/sys/net/ipv4/tcp_synack_retries
Enable Address Spoofing Protection
To prevent IP Spoof.

echo 1 > /proc/sys/net/ipv4/conf/all/rp_filter
Disable SYN Packet tracking
To prevent the system from using resources tracking SYN Packets.

sysctl -w net/netfilter/nf_conntrack_tcp_loose=0
IPTables
Drop Invalid Packets
Drop invalid packets with invalid or unknown status.

iptables -A INPUT -m state --state INVALID -j DROP
Block packets with bogus TCP flags
iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,SYN,RST,PSH,ACK,URG NONE -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,SYN FIN,SYN -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags SYN,RST SYN,RST -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags SYN,FIN SYN,FIN -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,RST FIN,RST -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,ACK FIN -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags ACK,URG URG -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags ACK,FIN FIN -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags ACK,PSH PSH -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL ALL -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL NONE -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL FIN,PSH,URG -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL SYN,FIN,PSH,URG -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL SYN,RST,ACK,FIN,URG -j DROP
Drop ICMP
To prevent Smurf Attack.

iptables -t mangle -A PREROUTING -p icmp -j DROP
Drop Fragments in all Chains
iptables -t mangle -A PREROUTING -f -j DROP
Limit connections per IP
iptables -A INPUT -p tcp -m connlimit --connlimit-above 18 -j REJECT --reject-with tcp-reset
Limit RST Packets
iptables -A INPUT -p tcp --tcp-flags RST RST -m limit --limit 2/s --limit-burst 2 -j ACCEPT
iptables -A INPUT -p tcp --tcp-flags RST RST -j DROP
Use of SYN-PROXY
iptables -t raw -A PREROUTING -p tcp -m tcp --syn -j CT --notrack
iptables -A INPUT -p tcp -m tcp -m conntrack --ctstate INVALID,UNTRACKED -j SYNPROXY --sack-perm --timestamp --wscale 7 --mss 1460
iptables -A INPUT -m state --state INVALID -j DROP
Prevent SSH Bruteforce
iptables -A INPUT -p tcp --dport ssh -m conntrack --ctstate NEW -m recent --set
iptables -A INPUT -p tcp --dport ssh -m conntrack --ctstate NEW -m recent --update --seconds 60 --hitcount 10 -j DROP
Prevent Port Scanner
iptables -N port-scanning
iptables -A port-scanning -p tcp --tcp-flags SYN,ACK,FIN,RST RST -m limit --limit 1/s --limit-burst 2 -j RETURN
iptables -A port-scanning -j DROP

# check out 
https://machinelearningmastery.com/multiple-model-machine-learning/
https://machinelearningmastery.com/one-vs-rest-and-one-vs-one-for-multi-class-classification/
https://machinelearningmastery.com/stacking-ensemble-machine-learning-with-python/
https://realpython.com/getting-started-with-django-channels/
https://trycatchdebug.net/news/1124453/reading-pcap-files-in-python
https://support.metageek.com/hc/en-us/articles/115000910348-Splitting-PCAP-Files-with-tcpdump
https://www.wireshark.org/docs/man-pages/tshark.html
https://stackoverflow.com/questions/8092380/export-pcap-data-to-csv-timestamp-bytes-uplink-downlink-extra-info
https://www.youtube.com/watch?v=uf8zJhnWALI&list=PLpbzVrYIIhHaLQEtiVtYhNlZnyV5mb5vp 

