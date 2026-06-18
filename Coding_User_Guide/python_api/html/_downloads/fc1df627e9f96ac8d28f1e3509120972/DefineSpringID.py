def DefineSpringID(shells):
        
	thickness = list()
	for shell in shells:
		prop = shell.get_entity_values(constants.RADIOSS, ("PID", ))
		ret_val = prop.get_entity_values(constants.RADIOSS, ("THICK", ))
		thickness.append(ret_val['THICK'])

	maximum = max(thickness)
	if maximum <= 1:
		vals = {"Name": "Maximum thickness less than " + str(maximum), 
				"PID": 500, 
				"TYPE": "SPR_BEAM 13", 
				"MASS": 0.5}
		ent = base.CreateEntity(constants.RADIOSS, 'PROP/SPR_BEAM', vals)
	else:
		vals = {"Name": "Maximum thickness greater than " + str(maximum), 
				"PID": 1000, 
				"TYPE": "SPR_BEAM 13", 
				"MASS": 1}
		ent = base.CreateEntity(constants.RADIOSS, "PROP/SPR_BEAM", vals)
	return ent 
