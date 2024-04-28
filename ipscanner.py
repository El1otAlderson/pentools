#scapy is powerful framework / library which i could create ip scanner based on arp broadcast. It doesnt use icmp protocol so its more easily to bypass basic firewalls and it works for almost every device in local network
#Thanks for chat gpt and tryhackme to give me a idea and help to create this program
#example of code python ipscanner.py eth0 192.168.1.0/24 ff:ff:ff:ff:ff:ff
# eth0 = interface of network card  192.x.x.x /24 = subnet ff:x:x:x: = broadcast mac address 
import sys
from scapy.all import *

if len(sys.argv) != 4:
    print("Usage: python script.py <interface> <ip_range> <broadcast_mac>")
    sys.exit(1)

interface = sys.argv[1]
ip_range = sys.argv[2]
broadcast_mac = sys.argv[3]

packet = Ether(dst=broadcast_mac) / ARP(pdst=ip_range)

ans, unans = srp(packet, timeout=2, iface=interface, inter=0.1)

print("Responses:")
for send, receive in ans:
    print(receive.sprintf("%Ether.src% - %ARP.psrc%"))
