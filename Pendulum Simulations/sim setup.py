# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 15:57:46 2023

@author: benkr
"""

def simdict():
    motor_active = [False, False]
    timer = [0, 0]
    duration = [0, 0]
    motor_rate = [0, 0]
    
    setup = {
        """lengths - need to be corrected (Nao dimensions)"""
        "rl": 151 + 7,
        "sl1": 16,
        "sl2": 19 + 5,
        "sl3": 17,
        "ll1": 16,
        "ll2": 6,
        "tl": 26,
        
        "bg": (400,200),
        
        """masses /kg"""
        "rm": 1.235 + 0.381/2,
        "sm1": 0.381/2,
        "sm2": 1.026,
        "sm3": 0.131*2 + 0.070 +0.390*2,
        "lm1": 0.292*2 + 0.134,
        "lm2": 0.162*2 + 0.134,
        "tm": 1.050 + 0.064 + 0.605 + 0.075 + 0.070,
    }
    
    centres = {
        "rc": (setup["bg"][0], setup["bg"][1] + setup["rl"]/2),
        "sc": (setup["bg"][0], setup["bg"][1] + setup["rl"] + setup["sl2"]/2),
        "lc": (setup["bg"][0] + setup["sl3"]/2, setup["bg"][1] + setup["rl"] + setup["sl2"] + setup["ll1"]/2),
        "tc": (setup["bg"][0] - setup["sl3"]/2, setup["bg"][1] + setup["rl"] + setup["sl2"] - setup["tl"]/2),
    }
        
    #these add the object to the simulation
    rod = Rod(centres["rc"], (0,setup["rl"]/2), (0,-setup["rl"]/2), setup["rm"])
    swing = Swing(centres["sc"], (0,-setup["sl2"]/2), (setup["sl1"]/2,-setup["sl2"]/2), (0,setup["sl2"]/2), (0,-setup["sl2"]/2), (-setup["sl3"]/2 -0.5,setup["sl2"]/2), (setup["sl3"]/2 -0.5,setup["sl2"]/2), setup["sm1"], setup["sm2"], setup["sm3"])
    leg = Leg(centres["lc"], (0, -setup["ll1"]/2), (0, setup["ll1"]/2), (0, setup["ll1"]/2), (setup["ll2"], setup["ll1"]/2), etup["lm1"], etup["lm2"])
    torso = Torso(centres["tc"], (0,-setup["tl"]/2), (0,setup["tl"]/2), 2)
    
    #fixed joints of simulation
    back = PinJoint(swing.body, torso.body, (-setup["sl3"]/2 -0.5,setup["sl2"]/2), (0,setup["tl"]/2))#second needs fixing to first
    front = PinJoint(swing.body, leg.body, (setup["sl3"]/2 -0.5,setup["sl2"]/2), (0, -setup["ll1"]/2))
    bottom = PinJoint(rod.body, swing.body, (0,setup["rl"]/2), (0,-setup["sl2"]/2))
    top = PinJoint(background, rod.body, setup["bg"], (0,-setup["r2"]/2))
    return {"pm_space":space, "motor_active":motor_active, "timer":timer, "duration":duration, "motor_rate":motor_rate}