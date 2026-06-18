import ansa
from ansa import base
from ansa import constants


def CheckRBE3_HEXA_RBE3():
	nastran = constants.NASTRAN
	#Collects all Spotwelds.
	concts = base.CollectEntities(nastran, None, 'SpotweldPoint_Type')
	for cnctn in concts:
		vals = ("X", "Y", "Z", "P1", "P2", "P3", "P4", "Status", "ID", "Error Class")
		ret = cnctn.get_entity_values(nastran, vals)
		#Initialize
		i = 0
		j = 0
		no_of_rbe = 0
		no_of_solids = 0
		if ret['Error Class'] == "RBE3-HEXA-RBE3":
			ents = base.CollectEntities(nastran, cnctn, "__ALL_ENTITIES__", False)
			#Loops through the Entities of each Spotwelds
			for ent in ents:
				type = ent._ansaType(nastran)
				if type == "RBE3":
					if i == 0:
						no_of_rbe = ent._id
						i = 1
					else:
						no_of_rbe = str(no_of_rbe) + "," + str(ent._id)
				if type == "SOLID":
					if j == 0:
						no_of_solids = ent._id
						j = 1
					else:
						no_of_solids = str(no_of_solids) + "," + str(ent._id)
		print("Connection with cid ", ret['ID'], " has RBE3s with ids: ", no_of_rbe, " and SOLIDs with ids: ", no_of_solids)
