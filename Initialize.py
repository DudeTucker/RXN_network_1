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


def initialize_reactions():
	rates, species, stoich = np.loadtxt('reactions.txt', delimter = '  ', dtype = str, unpack = True) # brings this in as arrays. 
	rates = list(rates)
	species = list(species)
	stoich = list(stoich) 				#makes these lists of strings

	reactions = []

	for i in range(len(rates)):
		rates[i]=eval(rates[i])
		species[i]=eval(species[i])
		stoich[i]=eval(stoich[i])       #makes these lists of lists

		forward_k=rates[i][0]			# this is pulling the first list of the rates data set jsut imported. position 0.
		reverse_k=rates[i][1]			# same, but for the second data position of the imported list 'rates'

		reactions.append(Reaction(i,species[i],forward_k, reverse_k))

	Parameters.reaction_list = reactions









