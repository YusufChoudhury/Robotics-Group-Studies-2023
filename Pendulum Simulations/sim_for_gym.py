'''this will be used in gym'''

'''get_angle does not work, need to fix to limit the torso movement like with leg'''
'''center of gravities of classes needs calculation'''
'''needs masses of robot components'''
'''need to add control systems for motor joints'''


import pymunk, sys
from pymunk.pygame_util import *
from pymunk.vec2d import Vec2d
import pygame
from pygame.locals import *
import numpy as np
from PIL import Image
from pymunk.pygame_util import DrawOptions



def angle(x1, x2, y1, y2, theta=0, phi=0):
    'angle between two points, can take away other angles to make it relative to other component'
    return np.arctan2(x2 -x1, y2 - y1) - theta - phi

def CoM(x1, x2, y1, y2, m1, m2):
    'center of mass'
    return ((m1*x1 + m2*x2)/2, (m1*y1 + m2*y2)/2)

class Rod:
    def __init__(self, pos, a, b, m, space, radius=4):
        'position of CoM, start, end, mass, radius(width)'
        self.body = pymunk.Body()
        self.body.position = pos
        self.radius = radius
        self.a = a
        self.b = b
        self.body.center_of_gravity = (0,0)
        self.shape = pymunk.Segment(self.body, self.a, self.b, radius)
        self.shape.mass = m
        self.shape.elasticity = 0
        self.shape.filter = pymunk.ShapeFilter(group=1)
        self.shape.color = (0, 255, 0, 0)
        space.add(self.body, self.shape)

class Leg:
    def __init__(self, pos, a1, b1, a2, b2, m1, m2, space, radius=3):
        'position of CoM, leg_start, leg_end, foot_start, foot_end,'
        ' leg_mass,  foot_mass, radius(width)'
        self.body = pymunk.Body()
        self.body.position = pos
        self.radius = radius
        self.a1 = a1
        self.b1 = b1
        self.a2 = a2
        self.b2 = b2
        self.body.center_of_gravity = (0,0)#needs calculation
        self.leg = pymunk.Segment(self.body, self.a1, self.b1, radius)
        self.leg.filter = pymunk.ShapeFilter(group = 1)
        self.leg.color = (0, 255, 0, 0)
        self.leg.mass = m1
        self.foot= pymunk.Segment(self.body, self.a2, self.b2, radius=radius)
        self.foot.filter = pymunk.ShapeFilter(group = 1)
        self.leg.mass = m2
        self.foot.color = (0, 255, 0, 0)
        space.add(self.body, self.leg, self.foot)

class Rotarylimitjoint:
    'stops swing moving out of control area i think'
    def __init__(self, b, b2, min, max, space, collide=True):
        joint = pymunk.constraints.RotaryLimitJoint(b, b2, min, max)
        joint.collide_bodies = collide
        space.add(joint)

class Simplemotor:
    'is added and removed at diffrent points to move a joint at a constant speed'
    def __init__(self, body1, body2, rate, space, switch="off"):
        'rate is angular velocity in radians'
        self.rate = rate
        self.body1 = body1
        self.body2 = body2
        self.simplemotor = pymunk.SimpleMotor(self.body1, self.body2, self.rate)
        space.add(self.simplemotor)
    def remove(self):
        space.remove(self.simplemotor)

class Pinjoint:
    def __init__(self, body1, body2, con1, con2, space):
        'two bodies and where to connect them by on each body'
        joint = pymunk.constraints.PinJoint(body1, body2, con1, con2)
        space.add(joint)

class Swing:
    def __init__(self,pos, a1, b1, a2, b2, a3, b3, m1, m2, m3, space, radius=10):
        'position of CoM, a=start, b=end, m=mass, 1/2/3=bar/vertical/base'
        self.body = pymunk.Body()
        self.body.position = pos
        s1 = pymunk.Segment(self.body, a1, b1 , radius=2) #bar  
        s1.filter = pymunk.ShapeFilter(group = 1)
        s1.mass = m1
        s2 = pymunk.Segment(self.body, a2, b2, radius=3)#vertical
        s2.filter = pymunk.ShapeFilter(group = 1)
        s2.mass = m2
        s3 = pymunk.Segment(self.body, a3, b3, radius=3)#base
        s3.filter = pymunk.ShapeFilter(group = 1)
        s3.mass = m3
        space.add(self.body, s1,s2,s3)

class Torso:
    def __init__(self, pos, a, b, m, space, radius=3):
        'position of CoM, a=start, b=end, m=mass'
        self.body = pymunk.Body()
        self.body.position = pos
        self.radius = radius
        self.a = a
        self.b = b
        self.body.center_of_gravity = (0,0)
        self.torso= pymunk.Segment(self.body, self.a, self.b , radius=radius)        
        self.torso.filter = pymunk.ShapeFilter(group = 1)
        self.torso.mass = m
        self.torso.color = (255, 0, 0, 0)
        space.add(self.body, self.torso)
'''
# rod_test = Rod((400 , 500), (0,-100) , (0,100), 5)
# PinJoint(background, rod_test.body, (400,400), (0,-100))


#lengths of components:
'hinge_height = 12'
r = 151+7
s1 = 16
s2 = 19+5
s3 = 17
l1 = 16
l2 = 6
t = 26

#start angle stuff
ta = np.pi/18#top angle
ba = np.pi/18#bottom angle
sta = np.sin(np.pi/18)
cta = np.cos(np.pi/18)

#centers of components:
bg = (400,200)#this is position of top hinge
rc = (bg[0], bg[1]+r/2)
sc = (bg[0], bg[1]+r +s2/2)
lc = (bg[0]+s3/2, bg[1]+r+s2+l1/2)
tc = (bg[0]-s3/2, bg[1]+r+s2-t/2)

#these add the object to the simulation, masses need revision
rod = Rod(rc, (0,r/2), (0,-r/2), 1235 +381/2)
swing = Swing(sc, (0,-s2/2), (s1/2,-s2/2), (0,s2/2), (0,-s2/2), (-s3/2 -0.5,s2/2), (s3/2 -0.5,s2/2), 0.381, 1.026, 2)
leg = Leg(lc, (0, -l1/2), (0, l1/2), (0, l1/2), (l2, l1/2), 0.5, 0.2)
torso = Torso(tc, (0,-t/2), (0,t/2), 2)

#fixed joints of simulation
back = Pinjoint(swing.body, torso.body, (-s3/2 -0.5,s2/2), (0,t/2))#second needs fixing to first
front = Pinjoint(swing.body, leg.body, (s3/2 -0.5,s2/2), (0, -l1/2))
bottom = Pinjoint(rod.body, swing.body, (0,r/2), (0,-s2/2))
top = Pinjoint(background, rod.body, bg, (0,-r/2))

rotation_lim = Rotarylimitjoint(rod.body,swing.body , -np.pi/4, np.pi/4)'''

