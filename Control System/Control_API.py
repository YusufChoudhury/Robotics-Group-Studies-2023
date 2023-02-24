"""
This file should:
- be written in python 2.7 syntax
- take the "action" from the "Controller.py" instance running on the lab PC and convert it into movement on NAO using the naoqi API.
- retrieve information from NAO about the angle and send it to the "Controller.py"
"""

import socket
from naoqi import ALProxy


# main loop - should'nt need to be changed much
def main(PORT_NUMBER = 10000,NAO_IP = "192.168.1.3"):
  
  TCP_connection = TCP_connect(PORT_NUMBER)
  NAO_connection = NAO_connect(NAO_IP)

  while True:
    action = get_action(TCP_connection)
    move_NAO(action)
    NAO_info = get_NAO_info(NAO_connection)
    send(NAO_info)
    
    
# -------------------------------------------------------- NAO stuff:  

# connect to NAO using its IP and port number and return the connection variable
def NAO_connect(NAO_IP):
  return None

# take the action in the [hip_angle,hip_angle_speed,knee_angle,knee_angle_speed] format and turn this into movement on NAO
def move_NAO(action):
  pass

# request the knee and hip angle from NAO and return it in the [hip_angle, knee_angle] format
def get_NAO_info(NAO_connection):
  return None


# -------------------------------------------------------- Client - server stuff

# initialise the connection between the client and the server using the port number
def TCP_connect(PORT_NUMBER):
  return None

# recieve the action info from the controller.py instance running on the lab PC and return this info in the:
# [hip_angle,hip_angle_speed,knee_angle,knee_angle_speed] format
def get_action(TCP_connection):
  
  return [hip_angle,hip_angle_speed,knee_angle,knee_angle_speed]


# send the NAO_info array in [hip_angle, knee_angle] format to the lab PC
def send(NAO_info):
  pass

  
main()
