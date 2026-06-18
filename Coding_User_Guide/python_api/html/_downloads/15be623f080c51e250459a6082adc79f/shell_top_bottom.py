import ansa
from ansa import base
from ansa import constants

# Draw each side of every Shell with the values (1, 2), if its id is even and (3, 4), if it is odd.
# (The first number of the tuple is the color of the top side of the Shell and the second number is the bottom side)
# Also, draw every Solid with the mod 3 of its id.
class Draw():
	def __init__(self, deck):
		self.values = {}
		self.deck = deck
	def start(self):
		self.values.clear()
	def end(self):
		return self.values
	def __call__(self, entity):
		ansa_type = entity.ansa_type(self.deck)
	        if ansa_type == 'SHELL':
			if entity._id % 2 == 0:
				self.values[entity] = (1, 2)
			else:
				self.values[entity] = (3, 4)
		elif ansa_type == 'SOLID':
			self.values[entity] = entity._id % 3

def nodal_thickness_draw_mode():
	deck = constants.ABAQUS
	draw_mode = base.FringeDrawMode('SHELLS TOP BOTTOM PLUS SOLIDS')
	draw_mode.fringe(deck=deck, element_type=('SHELL', 'SOLID'), mode='shell_top_bottom', draw=Draw(deck))
	draw_mode.enable()
