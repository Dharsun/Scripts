#!/usr/bin/env python

import requests
import re
import urlparse2





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




print("Example http(or)https ==http://scteng.co.in/")
target_url = raw_input("Enter url to Scan == ")
target_link = []

def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)

def craw(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = urlparse2.urljoin(url, link)
        if "#" in link:
            link = link.split("#")[0]
        if target_url in link and link not in target_link:
            target_link.append(link)
            print(link)
            craw(link)


craw(target_url)
