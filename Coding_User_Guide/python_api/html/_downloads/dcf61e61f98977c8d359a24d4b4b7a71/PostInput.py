import ansa
from ansa import base
    
def InputPost(filename, post_func_args):
	if post_func_args != "yes":
		return True

	with open(filename, 'r') as f:
		for line in f:
			if 'Model Id' in line:
				tokens = line.split(':')
				model_id = tokens[1].letters()
			elif 'LoadCase Name' in line:
				tokens = line.split(':')
				loadcase_name = tokens[1].letters()
	comment = "Model Id: " + model_id + "\n" + "LoadCase: " + loadcase_name
	base.SetGeneralComment(comment)
	return True
