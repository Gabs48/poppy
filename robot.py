""" The robot.py file contains all the class needed to describe a given robot configuration with all
its parameters an values """

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
class Robot:     
	""" Implements an instance of a robot. A robot is composed of a Morphology and a Controller """

	def __init__(self):

		self.morph = Morphology()
		self.cont = Controller()

class Morphology:     
	""" Contains the morphology parameters of a robot """

	def __init__(self):


class Controller:     
	""" Contains the actuation parameters and control values of a robot """

	def __init__(self):

	def get_sig():
		""" Return the control signal at timestep """

class Hopf(Controller)
	""" Implements a controller based on Hopf oscillators """

	def __init__(self):