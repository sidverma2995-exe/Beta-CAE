import time
import itertools

import ansa
from ansa import base
from ansa import session

def ImportV1FreeFormat(filename):
	session.New('discard')

	t1 = time.time()

	a = base.ImportV1()
	a.start()

	f = open(filename)
	line = f.readline()

	s = line.split()

	n_nodes = int(s[0])
	n_shells = int(s[1])
	n_solids = 0
	if len(s) == 3:
		n_solids = int(s[2])

	# Create Nodes
	nid = []
	x   = []
	y   = []
	z   = []

	n_count = 0

	for item in map(str.split, itertools.islice(f, n_nodes)):
		nid.append(n_count + 1)
		x.append(float(item[0]))
		y.append(float(item[1]))
		z.append(float(item[2]))
		
		n_count += 1

	a.create_nodes(nid, x, y, z)

	del nid, x, y, z
	# ~Create Nodes

	# Create Shells
	eid = []
	t   = []
	pid = []
	n1  = []
	n2  = []
	n3  = []
	n4  = []

	n_count = 0

	for item in map(str.split, itertools.islice(f, n_shells)):
		eid.append(n_count + 1)
		pid.append(1)
		n1.append(int(item[0]))
		n2.append(int(item[1]))
		n3.append(int(item[2]))
		n4.append(int(item[3]))
		if n3[n_count] == n4[n_count]:
			e_type = a.TRIA
		else:
			e_type = a.QUAD
		t.append(e_type)

		n_count = n_count + 1

	a.create_shells(eid, t, pid, n1, n2, n3, n4)

	del eid, t, pid, n1, n2, n3, n4
	# ~Create Shells

	# Create Solids
	if n_solids > 0:
		eid = []
		pid = []
		n1  = []
		n2  = []
		n3  = []
		n4  = []
		n5  = []
		n6  = []
		n7  = []
		n8  = []
		t   = []

		n_count = 0

		for item in map(str.split, itertools.islice(f, n_solids)):
			eid.append(n_count + 1)
			pid.append(2)
			n1.append(int(item[0]))
			n2.append(int(item[1]))
			n3.append(int(item[2]))
			n4.append(int(item[3]))
			n5.append(int(item[4]))
			n6.append(int(item[5]))
			n7.append(int(item[6]))
			n8.append(int(item[7]))

			if n5[n_count] == 0:
				e_type = a.TETRA
			elif n6[n_count] == 0:
				e_type = constans.HEOP
			elif n7[n_count] == 0 or n8[n_count] == 0:
				e_type = a.PENTA
			else:
				e_type = a.HEXA
			t.append(e_type)

			n_count = n_count + 1

		a.create_solids(eid, t, pid, n1, n2, n3, n4, n5, n6, n7, n8)

		del eid, pid, t, n1, n2, n3, n4, n5, n6, n7, n8
	# ~Create Solids

	f.close()

	a.build()
	a.finish()
	del a

	t2 = time.time()
	print("Time ImportV1FreeFormat: %f" % (t2-t1))
