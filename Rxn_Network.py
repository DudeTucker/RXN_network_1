import numpy as np 
import random
import math
import clock


import Parameters    # this means we are calling from parameters in real time, as in, we are not loading into RAM, therefore we must specify 'parameters.function', but, this also means we are changing the paramters file when we alter things here, as oppsed to changing it locally to a loaded version.
from Initialize import *
from Output import *
from Objects import *
from Reactions import *



def Main():

	random.seed(Parameters.run_seed)
	
	del Paramters.species[0:len(Parameters.sequences)]
	del Paramters.reactions[0:len(Parameters.reactions)]


	initialize_species()
	initialize_reactions()

	"""Main Gilliespie Loop"""
	while t<Parameters.tau_max:


