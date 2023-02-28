"""
This program should:
- be written with python 3.5+ syntax
- recieve the NAO info about its own joint angles
- give this information to the trained ML agent and save its decision / action
- send the action to the computer communicating with NAO

NOTE: WHEN WRITING THIS PROGRAM PLEASE RE-UPLOAD TO THE GITHUB AS Controller_V1.py and increment as needed
"""

from stable_baselines3 import PPO  

def connect(angle_info, HOST = '192.168.1.4', PORT = 10000):
    # The server's IP address: 192.168.1.100   For testing on local: 147.188.37.23
     # The port used by the server: 10000
    # Call this function when you need to send actions to the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print((HOST, PORT))
        s.connect((HOST, PORT))
        print('has connected')
        # For use with Python 2.7, change with....as s to s = and un-indent
        
        while True:
            try:
                from_server = s.recv(1024)
                commands = pickle.loads(from_server)
                
                if  commands == 'q':
                    break
                
                if not from_server:
                    print ('Disconnecting client...')
                    break 
                
                NAO_info = commands
                angle_info = angle_info
                # action, _states = model.predict(angle_info) - Machine learning agent makes the action decisions here
                action = get_action_DUMMY() # - dummy function to send example actions for testing purposes - should be replaced in final build
                s.sendall(actions)# Sends back the actions
                
            except:
               break
            
        s.close()


 # --------------------------------------------------------------------------------- main loop
def main():
 
 
  # model = PPO.load("test_PPO_model_data") - load the trained Machine Learning Agent here

  while True:
    angle_info = pickle.dumps(Encoders.sample(), protocol=0,fix_imports=True)
    connect(angle_info)


    
# ----------------------------------------------------------------------------------- comms

# fetch the angles from the decoders connected to the PC and return them in the [big,small] format
# the information from the four small encoders should be converted into a single angle so that the format is consistent with the simulation
def get_angle_info():
  return [large_encoder_angle,small_encoder_angle]


# retrieve the NAO information in the [hip_angle,knee_angle] format for the ML agent to see
def get_NAO_info(TCP_connection):
  return [hip_angle,knee_angle]


# send the action the agent has made to the Control_API.py instance communicating with NAO
def send(action):
  pass


# A dummy function for testing the control system - for example return values from a list of different angle values.
def get_action_DUMMY():
  return action
