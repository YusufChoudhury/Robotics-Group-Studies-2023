# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 14:51:21 2023

@author: princ
"""

############# TO BE USED IN CONJUNCTION WITH Encoder_Server.py #############

import socket,pickle

# The server's IP address: 192.168.1.100   For testing on local: 147.188.37.23
       # The port used by the server: 10000


def get_Encoder_data(HOST = '147.188.37.23', PORT = 10000):
    # The server's IP address: 192.168.1.100   For testing on local: 147.188.37.23
     # The port used by the server: 10000
    # Call this function when you need the encoder data from the server
    # Output Large_angle_array in degrees (1), Small_angle_array in degrees (4) , time (1) in seconds
    # For small encoders angles relative to the robot swinging forward - top +, bottom -, bottom +, top -
    # there is a required sampling rate of 0.1 seconds for getting encoder data   

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        # For use with Python 2.7, change with....as s to s = and un-indent
        
        ###### EXAMPLE that prints the encoder data when enter is pressed ########
        # Add code in here and call get_Encoder_data() to get encoder data #
        
        while True:
            commands = input('Enter for data/ q for disconnect')
            
            if  commands == 'q':
                break
            s.sendall(pickle.dumps('Hello'))
    
            data = s.recv(4096)
            commands = input(data)
            
        s.close()
    return data

