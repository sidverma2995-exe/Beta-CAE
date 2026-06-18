import ansa
from ansa import base

def TestPrePostOutputScript(conf, arg):
    
	if arg["UserArgs"]:
		print("arg['UserArgs']: " + arg["UserArgs"])
  
	all_types_of_ents = base.TypesInCategory (0, "__ALL_ENTITIES__")
	with open("include_log.txt", 'w') as f:
		includes_of_configuration = base.GetConfigurationIncludes(conf)
		for incl in includes_of_configuration:
			f.write ("\n***************\nINCLUDE " + incl._name + ":\n")
			for type in all_types_of_ents:
				ents = CollectEntities (0, incl, type)
				f.write (len(ents) + " " + type + "s\n")
