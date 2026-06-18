import math
class Point:
	""" A class that stores the x, y, z coordinates of a point,
	with a method that calculates the distance from the origin and
	a method that prints the description of the class"""

	def __init__(self, x_coord, y_coord, z_coord):
		"""This is the constructor of the class"""
		self.x = x_coord
		self.y = y_coord
		self.z = z_coord

	def distFromOrigin(self):
		"""Method that calculates the distancefrom the origin"""
		dist = math.sqrt(self.x**2 + self.y**2 + self.z**2)
		return dist

	def __repr__(self):
		return 'A point with X: ' + str(self.x) + ' Y: '+str(self.y) + ' Z:'+ str(self.x)


def main():
	myPoint = Point(100.57, 786.46, 436.89) #creation of class instance myPoint
	print(myPoint.x) #access the value of attribute x
	myPoint.x = 120.74 #assign new value
	distance = myPoint.distFromOrigin()
	print('The distance from the origin is: ' + str(distance))
	#In order to print the description of the object
	print(myPoint) #This will print the return of the __repr__
