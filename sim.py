""" The simulation.py file contains classes concerning the simulation as the simulation parameters,
a description of the world environment but also the simulation flow (Open Loop or Closed loop) """

# Imports

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
class World:
	"""
	Describes the simulation parameters and environment
	"""

class Simulation:     
	"""
	Implements an instance of a robot. A robot is composed of a Morphology and a Controller
	"""

	def __init__(self):

		self.world = World()
		self.robot = Robot()


class OLSimulation(Simulation):     
	"""
	Contains the morphology parameters of a robot
	"""

class CLSimulation(Simulation):     
	"""
	Contains the actuation parameters and control values of a robot
	"""
