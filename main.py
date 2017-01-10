#!/usr/bin/env python2

""" This is the main file to execute for testing biped locomotion of Poppy on VRep """

# Imports
import time
import math

from pypot.vrep import from_vrep
from poppy.creatures import PoppyHumanoid

# Additionnal information
__author__ = "Gabriel Urbain"
__copyright__ = "Copyright 2017, Human Brain Projet, SP10"

__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Gabriel Urbain"
__email__ = "gabriel.urbain@ugent.be"
__status__ = "Research"
__date__ = "January 10th, 2017"

# Content
if __name__ == "__main__":

	print("-- Init connection with VRep and create instance of Poppy --")
	poppy = PoppyHumanoid(simulator='vrep')

	amp = 30 # in degrees
	freq = 0.5 # in Hz

	t0 = time.time()

	print("-- Start actuating --")
	while True:
	    t = time.time()
	    
	    # run for 10s
	    if t - t0 > 10:
	        break

	    poppy.head_z.goal_position = amp * math.sin(2 * 3.14 * freq * t)
	    
	    time.sleep(0.04)

# TO DO:
# Choose between simulation (+ conf file or reload sim.pkl)
# or optim (+conf file or reload optim.pkl)