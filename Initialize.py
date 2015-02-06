import math
import numpy as np
from operator import itemgetter
import random
import matplotlib.pyplot as plt
import Output

from Objects import *
import itertools



def initialize_species():
	from Parameters import number_of_species, number_of_reactions

	species = []

	for i in range(number_of_species): 			# this generates a loop beteen 0 and the number of species
		if i ==0 or i ==1: 						# if species id = 0 or 1 then:

			speices.append(Speices(i, 10.0)) 	# give it a concentration of 10. (this arguments come fromt he object we set up)

		else:
			speices.append(Speices(i, 0.0))  	# if it is not a species = 0 or 1, give it a conc of 0

	Parameters.species_list = species 			# send this list to parameters
