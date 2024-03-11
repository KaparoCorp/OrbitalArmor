# This is a Project about DOS and DDOS ATTACK detection system using machine learning 

# Key words
1. DOS - Denial Of Service Attack
2. DDOS - Distributed Denial Of Service Attack
3. Network Scanning-

## Type of Dos Attacks 
1. Smurf attack --> The attacker sends Internet Control Message Protocol broadcast packets to a number of hosts with a spoofed source Internet Protocol(IP) address that belongs to the target machine. The recipents of these spoofed packets will then respond, and the targeted host will be flooded with those responses.
   
2. SYN flood --> Occurs when an attacker sends a request to connect to the target server but does not complete th connection through what is known as a three-way handshake -- a mehtod used in a Transmission Control Protocol(TCP/IP) network  to create a connection between a local host/client and server. The incomplete handshke leaves the connected port in an occupied status and unavailable for further requests. An attacker will continue to send requests, saturating all open ports, so that legitimate users cannot connect. 
   
3. Ping of Death (ICMP Flood)
4. Buffer Overflow Attack
5. Teardrop Attack 

### What is a denial of service attack?
DOS Attack--> Uses one internet connected device/network to flood the victims computer with malicious traffic so that when legitimate users are unable to access information systems, devices, or other network resources due to the actions of a malicious cyber threat actor.

Services affected may include email, websites, online accounts(Banking), or other services that rely on the affected computer or network. Can cost an organization both time and money while their resources and services are inaccessible.


DDOS --> Uses multiple internet connections to render the victims network inaccessible to them. DDos atackers often leverage the use of a botnet.DDos attacks have increased in magnitude as more and more devices come online through the Internet of Things(IoT)
IoT devices use default passwords and do not have sound security postures, making them vulnerable to compromise and exploitation.Infextion of IoT device often goes unnoticed by users, and an attacker could easily compromise hundreds of thousands of these devices to conduct a high-scale attack without the device owners' knowledge.


### Tools for DOS Attacks
1. Low Orbit Ion Cannon.
2. Ping 
   
   

### Tools for DDOS Attacks
1. Botnet
2. Cloud Computing power in Botnets
   
### Methods
1. Application layer Attack
2. Volumetric Attack
3. Fragmentation Attack
4. Protocal Based Attack
   
# This is a breakdown of how I made the DOS Attack Detection system using machine learning

Requirements can be downloaded using the requirements.txt file and pip using python 

``` python3 -m pip install -r requirements.txt ```

For this project I have chosen to use python 3.10.12 and can be installed form their website python.org, pandas ,sciPy, NumPy,Matplotlib and Tensorflow. 


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
https://www.youtube.com/watch?v=uf8zJhnWALI&list=PLpbzVrYIIhHaLQEtiVtYhNlZnyV5mb5vp 

