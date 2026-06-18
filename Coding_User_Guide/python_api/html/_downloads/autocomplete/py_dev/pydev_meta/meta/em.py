from __future__ import annotations
from typing import Iterable, Callable, Any
import warnings
import typing_extensions
from . import annotations, boundaries, connections, coordsystems, elements, em, groups, isofunctions, materials, models, nodes, nvh, overlay, pages, parts, planes, plot2d, report, results, sections, spreadsheet, tdk, utils, visuals, vr, windows

class Farfield():

	"""

	Class for farfields.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import em
		
		
		def main():
		    f = em.Farfield(name="Bistatic RCS", model_id=0)
		    print(f.name)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Name of the farfield.

	"""

	def get_model(self) -> models.Model:

		"""

		This method gets the model of the farfield.


		Returns
		-------
		models.Model
			Upon success, it returns an object of type Model referring to the model of the node. Upon failure, it returns None.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import em
			
			
			def main():
			    far = em.Farfield(name="Bistatic RCS", model_id=0)
			    m = far.get_model()
			    print(m)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def get_integral(self) -> float:

		"""

		This method gets the integral of the farfield.


		Returns
		-------
		float
			Upon success, it returns the integral of the farfield. Upon failure, it returns None.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import em
			
			
			def main():
			    far = em.Farfield(name="Bistatic RCS", model_id=0)
			    integral = far.get_integral()
			    print(integral)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Farfield entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import em
			
			
			def main():
			    f = em.Farfield(name="Bistatic RCS", model_id=0)
			    can_use = f.is_usable()
			    print(can_use)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def __init__(self, name: str, model_id: int) -> None:

		"""

		Farfield object constructor. The constructor will create a Python Farfield object that represents an existing META Farfield. The arguments must identify an existing META Farfield.


		Parameters
		----------
		name : str
			The name of the Farfield.

		model_id : int
			The id of the Model.

		Returns
		-------
		None

		"""


	def get_phi(self) -> float:

		"""

		This method gets the phi angle of the Farfield, if the Farfield is bistatic.


		Returns
		-------
		float
			Upon success, it returns a float value being the phi angle of the bistatic Farfield. 
			Upon failure, it returns None.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import em
			
			
			def main():
			    far = em.Farfield(name="Bistatic RCS", model_id=0)
			    print(far.name, far.get_phi())
			
			
			if __name__ == "__main__":
			    main()


		"""


	def get_theta(self) -> float:

		"""

		This method gets the theta angle of the Farfield, if the Farfield is bistatic.


		Returns
		-------
		float
			Upon success, it returns a float value being the theta angle of the bistatic Farfield. 
			Upon failure, it returns None.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import em
			
			
			def main():
			    far = em.Farfield(name="Bistatic RCS", model_id=0)
			    print(far.name, far.get_theta())
			
			
			if __name__ == "__main__":
			    main()


		"""


	def set_phi(self, value: float) -> None:

		"""

		This method sets the phi angle of the Farfield, if the Farfield is bistatic.


		Parameters
		----------
		value : float
			The phi angle

		Returns
		-------
		None
			Returns None

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import em
			
			
			def main():
			    far = em.Farfield(name="Bistatic RCS", model_id=0)
			    far.set_phi(100.0)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def set_theta(self, value: float) -> None:

		"""

		This method sets the theta angle of the Farfield, if the Farfield is bistatic.


		Parameters
		----------
		value : float
			The phi angle

		Returns
		-------
		None
			Returns None

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import em
			
			
			def main():
			    far = em.Farfield(name="Bistatic RCS", model_id=0)
			    far.set_theta(100.0)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def create_plot(self, angle: str, angle_value: float, window: windows.Window, attached: bool=True, axis_auto_update: str='both') -> None:

		"""

		This method creates a farfield plot.


		Parameters
		----------
		angle : str
			Type of the angle. Accepted values are:
			'phi',
			'theta'

		angle_value : float
			The angle value

		window : windows.Window
			A 2d Window object

		attached : bool, optional
			Checks whether the plot wil be attached to the Farfield or not

		axis_auto_update : str, optional
			Axis auto update. Accepted values are:
			'both',
			'none',
			'xaxis',
			'yaxis'

		Returns
		-------
		None
			Returns None

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import em, windows
			
			
			def main():
			    w = windows.Create2DPlotWindow("2d")
			    f = em.Farfield(name="Bistatic RCS", model_id=0)
			    f.create_plot("theta", 5, w, True, "both")
			
			
			if __name__ == "__main__":
			    main()


		"""

