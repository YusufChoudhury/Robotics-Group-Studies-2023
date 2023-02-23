    def holding(self, limb, centre, width):
        return ((1-(((self.simulation_data["pm_space"].bodies[limb].angle - self.simulation_data["pm_space"].bodies[1].angle) - centre) / width))**4) * 90*abs(np.sin(self.simulation_data["pm_space"].bodies[limb].angle))

    def effort(self):
        k4 = 1
        k5 = 1
        k6 = 1
        k7 = 1
    
        leg_acc = angular_velocity_leg / time
        torso_acc = angular_velocity_torso / time
        leg_hold = holding(self, 2, centre, width)
        torso_hold = holding(self, 3, centre, width)
        return k4*leg_acc + k5*leg_hold + k6*torso_acc + k7*torso_hold
        