import ansa
from ansa import base
from ansa import constants

class Draw():
	def __init__(self, deck):
		self.values = {}
		self.deck = deck
	def start(self):
		self.values.clear()
	def end(self):
		return self.values
	def __call__(self, entity):
		ret = entity.get_entity_values(self.deck, ('G1', 'G2', 'G3', 'G4', 't1', 't2', 't3', 't4'))
		self.values[ret['G1']] = ret['t1']
		self.values[ret['G2']] = ret['t2']
		self.values[ret['G3']] = ret['t3']
		if 'G4' in ret: # QUAD
			self.values[ret['G4']] = ret['t4']

def nodal_thickness_draw_mode():
	deck = constants.ABAQUS
	draw_mode = base.FringeDrawMode('Nodal Thickness')
	draw_mode.fringe(deck=deck, element_type='SHELL', mode='node', draw=Draw(deck))
	draw_mode.enable()


