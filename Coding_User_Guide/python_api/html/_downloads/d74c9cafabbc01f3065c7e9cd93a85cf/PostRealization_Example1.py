import ansa
from ansa import base

def PostRealization_Example1(cnctn, proj, proj_ents, interfaces, bodies, misc):
    
	flange = 1
	for point in proj:
		print("Projection on flange " + str(flange) + " : " + str(point[0]) + ", " + str(point[1]) + ", " + str(point[2]))
		flange += 1
        
	flange = 1
	for ents in proj_ents:
		for ent in ents:
			type = base.GetEntityType(0, ent)
			print("Projection ent on flange " + str(flange) + " : " + type + " ID: " + ent._id)
		flange += 1
        
	flange = 1
	for ents in interfaces:
		for ent in ents:
			type = base.GetEntityType(0, ent)
			print("Interface ent on flange " + str(flange) + " : " + type + " ID: " + ent._id)
		flange += 1
        
	flange = 1
	for ents in bodies:
		for ent in ents:
			type = base.GetEntityType(0, ent)
			print("Body ent on flange " + str(flange) + " : " + type + " ID: " + ent._id)
		flange += 1
        
	for i_item, item in enumerate(misc):
		print("Misc item " + str(i_item+1) + "; Type: " + str(item.__class__) + "; Value: " + str(item))
