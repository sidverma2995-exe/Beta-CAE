import ansa
from ansa import base
from ansa import constants
import math

def PostRealization_Example2(cnctn, proj, proj_ents, interfaces, bodies, misc):
	D = float(misc[0])
	A = math.pi*D**2/4
	I1 = I2 = math.pi*D**4/64
	J = math.pi*D**4/32
	existing_pbeams = base.CollectEntities(constants.NASTRAN, None, "PBEAM")
	prop_id = False
	for prop in existing_pbeams:
		tokens = prop._name.split("=")
		if len(tokens)>1 and tokens[1]==str(D):
			prop_id = prop._id

	if not prop_id:
		vals = {"Name": "SPW_SPIDER_D=" + str(D), "A(A)": A, "I1(A)": I1, "I2(A)": I2, "J(A)": J}
		new_pbeam_ent = base.CreateEntity(constants.NASTRAN, "PBEAM", vals)
		prop_id = new_pbeam_ent._id

	for ents in bodies:
		for ent in ents:
			if base.GetEntityType(constants.NASTRAN, ent)=="CBAR":
				ret = base.ChangeElemType(constants.NASTRAN, ent, target_name = "CBEAM", pid = prop_id)
				if ret:
					return -1 #Failure. Erase-FE.

