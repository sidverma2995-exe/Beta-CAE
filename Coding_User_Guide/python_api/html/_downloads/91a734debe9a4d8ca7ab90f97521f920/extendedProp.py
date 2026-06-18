import ansa
from ansa import base
from ansa import constants

class extendedProp(ansa.base.Entity):
	"""Subclassing the entity object of type ELEMENT_SHELL. We extend
	its behavior to return the cog and the number of Elements"""

	def __init__(self, deck, id, type):
		super().__init__(deck, id, type)

	def CalculateCog(self):
		return base.Cog(self)

	def ElementNumber(self):
		ents = base.CollectEntities(constants.LSDYNA, self, "ELEMENT_SHELL")
		return len(ents)

def main():
    
	ents = base.CollectEntities(constants.LSDYNA, None, "SECTION_SHELL")
	extended = list()
	for ent in ents:
		extended.append(extendedProp(constants.LSDYNA, ent._id, 'SECTION_SHELL'))
        
	for item in extended:
		(x, y, z) = item.CalculateCog()
		num = item.ElementNumber()
		print('cog: %f, %f, %f' % ( x, y, z) + ', number of elements: ' + str(num))

