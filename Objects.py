#Python Modules
import numpy as np

###################################################################################################

class Species(object):   		
    """A Polymeric Sequence"""
    
    def __init__(ID, conc, reactant_for, product_of):			# every class must contain an __init__ which generates an object of that class. I can put addition def:'s here, but i must have def: __init__'
        self.ID = ID						# One letter string
        self.conc = conc					# float
        #self.reactant_for = reactant_for	#[]	
        #self.product_of = product_of		#[]

###################################################################################################

class Species(reaction):
    """A reaction"""
    
    def __init__(ID, products, reactants, k_forward, k_reverse):
        self.ID = ID						#integer  (variable type)
        self.products = products			#[]
        self.reactants = reactants			#[]
        self.k_forward = k_forward			#float
        self.k_reverse = k_reverse			#float


###################################################################################################





