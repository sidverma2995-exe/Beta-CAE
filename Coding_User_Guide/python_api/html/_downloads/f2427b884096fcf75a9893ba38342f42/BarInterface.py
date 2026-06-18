def BarInterface(GEB_BC, FromRepr, FromSearch, diam):
	all_search_nodes = len(FromSearch)
	radius = float(diam)/2
	area = 3.14*radius**2
    
	#Get the id of the representation node.
	repr_id = FromRepr[0]._id
    
	#Create a PBAR property.
	new_prop = base.CreateEntity(constants.NASTRAN, 'PBAR', {"A":area})
	ret2 = base.GetEntityCardValues(constants.NASTRAN, new_prop, ("PID",))
	for i in range(all_search_nodes):
		#Get the id of each search node.
		search_id = FromSearch[i]._id
		#Create the bar.
		vals = {"N1": repr_id, "N2": search_id, "IPART": new_prop._id, "x1": 1}
		base.CreateEntity(constants.PAMCRASH, "BEAM", vals)

