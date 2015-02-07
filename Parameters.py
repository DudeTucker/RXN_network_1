S#Python Modules
from math import sqrt, pi, pow
import os

#####################################################################################################
run_seed = 31500
Total_runs = 1              #Number of experimental runs - used for cluster computing.


"""System Parameters & Output Specifications"""
tau_max = 1000                  # max simulation time (in dimensionless time units)
t_frequent = 2.0 				# how often data is output
number_of_reactions = 3 		
number_of_species = 7


species_list = [] 				#the list holding the species information
reaction_list = []



Propensities = []