#!/usr/bin/python
"""
Getting the value for  the interface and mac addr to a variable and then pass the value to the command directly

we can give value in as a argument in a command line using sys modules 
or with an option with help and switch we use optparse module 
python macchanger.py --interface wlan0 --mac 11:aa:dd:ff:gg:hh
python macchanger.py --help to print help
"""
import subprocess
import optparse
import re

def get_argument():
    """ methode to get argument """
    parser=optparse.OptionParser()	
    parser.add_option("-i","--interface",dest="interface",help="Interface to change the mac address")
    parser.add_option("-m","--mac",dest="new_mac",help="add new mac address")
    (options,arguments) = parser.parse_args() #to get arg input by user

    if not options.interface:
	#code to handle error
	
        parser.error("[-] Specify an Interface use python macchanger --help for more details")
    elif not options.new_mac:
	#code to handle error
	    parser.error("[-] Specify an MacAddr use python macchanger --help for more details")
        
    return options


def getmac(interface):
    """  methode to get mac address """
    ifconfig_result = subprocess.check_output(["ifconfig",interface])

    mac_address_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)    #current mac address

    if mac_address_result:
	    return mac_address_result.group(0)
    else:
        print('[-] could not read MAC address')

        
def macchanger(interface,macaddr):
    """ methode to change mac address """
    subprocess.call(["ifconfig",interface,"down"])   #to use system commandes 
    subprocess.call(["ifconfig",interface,"hw","ether",macaddr])
    subprocess.call(["ifconfig",interface,"up"])





options= get_argument() 
current_mac=getmac(options.interface)
print('current_mac'+ str(current_mac))

macchanger(options.interface,options.new_mac)
final_mac = getmac(options.interface)

if final_mac == options.new_mac :
    print ("Mac Address Successfully Changed with new one " + final_mac)
else:
    print ("Error Occured Fix It")
