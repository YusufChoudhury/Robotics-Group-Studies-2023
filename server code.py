# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 17:24:55 2023

@author: princ
"""
import socket, pickle, numpy as np

HOST = '192.168.1.4'  # The server's IP address: 192.168.1.100   For testing on local: 147.188.37.23
PORT = 10000            # The port used by the server: 10000 

print ('Server IP: ', HOST)

while True:
    print ('Waiting for client connection...')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT)) 
        s.listen()
        conn, addr = s.accept()
        
        with conn:
            
            
            print('Connected by', addr)
            while True:
                
                try:
                    from_client = conn.recv(1024)
                    commands = input(pickle.loads(from_client))
                    
                    commands = input('Enter message/ q for disconnect')
                    if  commands == 'q':
                        break
                    
                    
                    if not from_client:
                        print ('Disconnecting client...')
                        break 
            
                    data = np.ones(10) 
                    #pickle.dumps(Encoders.sample(), protocol=0,fix_imports=True) # Serialises the data to prepare to send the encoder data
                    #data = pickle.dumps(commands)
                    conn.sendall(data)# Sends back the current encoder data
                    
                except:
                    break
                
                
            print('Connection lost')
            s.close()
            break
            
    #if input('Turn Server off? y/n') == 'y':
        # You need to type anything other that y on the server before connecting a new client 
        #break
    
#Encoders.close()

