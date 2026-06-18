from ansa import base 
from ansa import constants
from ansa import cad

def CAD_Translate():
	ents = base.CollectEntities(constants.NASTRAN, None, 'ANSAPART')
	lines = ents[0]._comment.split("\n")
	for line in lines:
		m = line.split(":")
		attribute_name = m[0].strip()
		if attribute_name == "PartNumber":
			module_id = m[1].strip()
			print(module_id)
		elif attribute_name == "Revision":
			version = m[1].strip()
			print(version)
