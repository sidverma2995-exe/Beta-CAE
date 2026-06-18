import os

def OutputPost(filename, post_func_args):
	fw = open(filename + "_temp", "w")
	fw.write("$ Some user comments")
	fr = open(filename, "r")
    
	for line in fr:
		fw.write(line)

	fw.close()
	fr.close()
	os.rename(filename + "_temp", filename)
