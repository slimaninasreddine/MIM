#!/usr/bin/env python
import netfilterqueue

def process_packet(packet):
	print(packet)
#	packet.accept()   #forward the packet to the destination
#    packet.drop() # cut the packet to the destination 

queue = netfilterqueue.NetfilterQueue() #creat instance
queue.bind(0,process_packet)        #connect instance and give process for connect with each packet
queue.run()