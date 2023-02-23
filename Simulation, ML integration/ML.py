# Import relevent libraries
from Sim import setup_simulation, perform_action, get_action
import pygame
import numpy as np
import gym
from pymunk.pygame_util import DrawOptions


# Create gym environment - Contains the machine learning code and the simulation code:
class CustomEnv(gym.Env):

    # Initialising the environment - SINGLE SETUP FUNCTION CALL to be written by simulations team:
    def __init__(self, env_config={}):
        self.simulation_data = setup_simulation()

    # The actual bit where the simulation happens
    def step(self, action=np.zeros((4), dtype=np.single)):
        self.simulation_data = perform_action(self, action, self.simulation_data)
        self.simulation_data["pm_space"].step(1 / 1000)
        self.leg_angle = 180 / np.pi * (self.simulation_data["pm_space"].bodies[3].angle - self.simulation_data["pm_space"].bodies[3].angle)

        observation, reward, done, info = 0., 0., False, {}
        return observation, reward, done, info

    # Initialise the renderer (NOT RELEVENT TO SIMULATIONS)
    def init_render(self):
        pygame.init()
        self.window = pygame.display.set_mode((1000, 500))
        self.simulation_data["pm_space"].gravity = 0, 981
        self.options = DrawOptions(self.window)
        self.clock = pygame.time.Clock()

    # Render the state of the simulation (NOT RELEVENT TO SIMULATIONS)
    def render(self):
        self.window.fill((255, 255, 255))
        self.simulation_data["pm_space"].debug_draw(self.options)
        pygame.display.update()

    # Reset the simulation for the next training run (NOT RELEVENT TO SIMULATIONS)
    def reset(self):
        pass

# Fetch pygame events
def get_events():
    get_event = pygame.event.get()
    for event in get_event:
        if event.type == pygame.QUIT:
            pygame.quit()
    return pygame.key.get_pressed()


# Main loop - actually runs the code
def main():
    # Initialise the simulation:
    environment = CustomEnv()
    environment.init_render()

    # Run the simulation:
    while True:
        keys_pressed = get_events()
        action = get_action(keys_pressed)

        # Step the simulation, then render the result (rendering in pymunk)
        environment.step(action)
        environment.render()


main()
