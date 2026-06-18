import ansa
from ansa import base, constants

def PreOutput(filename, pre_func_args):
	props = base.CollectEntities(constants.LSDYNA, None, 'SECTION_SHELL')
	for prop in props:
		if base.GetEntityCardValues(constants.LSDYNA, prop, ('T1',))['T1'] == 1.0:
			base.SetEntityCardValues(constants.LSDYNA, prop, {'MID': int(pre_func_args)})
	return True
