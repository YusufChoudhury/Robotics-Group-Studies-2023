"""
This program should:
- be written with python 3.5+ syntax
- recieve the NAO info about its own joint angles
- give this information to the trained ML agent and save its decision / action
- send the action to the computer communicating with NAO
"""

from stable_baselines3 import PPO


 # --------------------------------------------------------------------------------- main loop
def main():
  TCP_connection = TCP_connect(SERVER_IP, PORT_NUMBER)
  # model = PPO.load("test_PPO_model_data") - load the trained Machine Learning Agent here

  while True:
    angle_info = get_angle_info()
    NAO_info = get_NAO_info(TCP_connection)
    # action, _states = model.predict(angle_info) - Machine learning agent makes the action decisions here
    action = get_action_DUMMY() # - dummy function to send example actions for testing purposes - should be replaced in final build
    send(action)

    
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
