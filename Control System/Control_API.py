"""
This file should:
- be written in python 2.7 syntax
- take the "action" from the "Controller.py" instance running on the lab PC and convert it into movement on NAO using the naoqi API.
- retrieve information from NAO about the angle and send it to the "Controller.py"
"""

import socket
from naoqi import ALProxy


def main(PORT_NUMBER = 10000,NAO_IP = "192.168.1.3"):
  
  TCP_connection = TCP_connect(PORT_NUMBER)
  NAO_connection = NAO_connect(NAO_IP)

  while True:
    action = get_action(TCP_connection)
    move_NAO(action)
    NAO_info = get_NAO_info(NAO_connection)
    send(NAO_info)
    
# -------------------------------------------------------- connection functions:  
def TCP_connect(PORT_NUMBER):
  return None

def NAO_connect(NAO_IP):
  return None


# -------------------------------------------------------- movement and info stuff
def get_action(TCP_connection):
  return None

def move_NAO(action):
  pass

def get_NAO_info(NAO_connection):
  return None

def send(NAO_info):
  pass

  
  
main()
