from __future__ import annotations
from typing import Iterable, Callable, Any
import warnings
import typing_extensions

def Quit(status: int) -> int:

	"""

	This function quits the current file and exits the program.

	Parameters
	----------
	status : int, optional
		The exit code status of the application. (Default = 0)

	Returns
	-------
	int
		Returns 0 in all cases.

	Examples
	--------
	::

		import sdm
		from sdm import session
		
		
		def main():
		    session.Quit()


	"""

@typing_extensions.deprecated("Deprecated since version 23.1.0.Use utils.GetProcessSystemMetrics instead.")
def PrintMemoryUsage(prefix: str) -> int:

	"""
	.. deprecated:: 23.1.0
		Use :py:func:`utils.GetProcessSystemMetrics` instead.


	Will print the application's current memory usage.

	Parameters
	----------
	prefix : str, optional
		If the prefix argument is given, then it will precede the printed text.

	Returns
	-------
	int
		Returns 1 on success and 0 on failure.

	Examples
	--------
	::

		import sdm
		from sdm import session
		
		
		def main():
		    session.PrintMemoryUsage()


	"""

	warnings.warn("Deprecated since version 23.1.0.Use utils.GetProcessSystemMetrics instead.", DeprecationWarning)

def ProgramArguments() -> list[str]:

	"""

	This function retrieves the command line arguments of the program.

	Returns
	-------
	list[str]
		Returns a list containing the program arguments.

	Examples
	--------
	::

		import sdm
		from sdm import session
		
		
		def main():
		    m = session.ProgramArguments()
		    print("There are ", len(m), " arguments")


	"""

@typing_extensions.deprecated("Deprecated since version 23.1.0.Use utils.GetProcessSystemMetrics instead.")
def GetFreePhysicalMemory() -> int:

	"""
	.. deprecated:: 23.1.0
		Use :py:func:`utils.GetProcessSystemMetrics` instead.


	Returns the free physical memory at the time of this function's call in kilobytes (1024 bytes).

	Returns
	-------
	int
		Returns the free physical memory on success and 0 on failure.

	Examples
	--------
	::

		import sdm
		from sdm import session
		
		
		def main():
		    m = session.GetFreePhysicalMemory()
		    print(m)


	"""

	warnings.warn("Deprecated since version 23.1.0.Use utils.GetProcessSystemMetrics instead.", DeprecationWarning)

def BetaClearVariable(name: str) -> bool:

	"""

	This function frees the memory from the given beta variable.

	Parameters
	----------
	name : str
		The name of the beta variable.

	Returns
	-------
	bool
		True if operation was successful, False otherwise.

	Examples
	--------
	::

		import pickle
		import sdm
		from sdm import session
		
		
		def main():
		    beta_var_name = "a"
		    p = 1
		    v = pickle.dumps(p)
		    session.BetaSetVariable(beta_var_name, v)
		    v = session.BetaGetVariable(beta_var_name)
		    p = pickle.loads(v)
		    print(p)
		    session.BetaClearVariable(beta_var_name)
		    v = session.BetaGetVariable(beta_var_name)
		    if v == None:
		        print('Variable "' + beta_var_name + '" cannot be retrieved')


	"""

def BetaGetVariable(name: str, match: int) -> object:

	"""

	Ansa script can store user data and address them by a name.
	These data are NOT volatile as script variables and can be accessed either from different scripts or whenever a script is run.
	This function allows the user to retrieve data stored under a user specified name.
	Wildcards can also be used ("*", "?", "[...]").

	Parameters
	----------
	name : str
		The name of the beta variable to be retrieved.

	match : int, optional
		Control the matching mode of the name lookup.
		Values are:
		-constants.ENM_EXACT: an exact match (default)
		-constants.ENM_WILDCARD: a wildcard match

	Returns
	-------
	object
		The function returns the Beta Variable if the variable is found. It returns None otherwise.
		
		If match=constants.ENM_WILDCARD is used, it returns a dictionary with key the variable name and data the variable value.
		The dictionary is empty if no variables matching the wildcard expression were found.

	Raises
	------
	ValueError
		If an unknown match value is given.

	See Also
	--------
	sdm.session.BetaSetVariable

	Examples
	--------
	::

		import pickle
		
		import sdm
		from sdm import constants
		from sdm import session
		
		
		def main():
		    p = 1
		    v = pickle.dumps(p)
		    session.BetaSetVariable("a", v)
		    v = session.BetaGetVariable("a")
		    p = pickle.loads(v)
		    print(p)
		
		    p = 2
		    v = pickle.dumps(p)
		    session.BetaSetVariable("AB", v)
		
		    print("Variables matching *")
		    vars = session.BetaGetVariable("*", constants.ENM_WILDCARD)  # returns all variables
		    for key, value in vars.items():
		        p = pickle.loads(value)
		        print("Name: {} Value: {}".format(key, p))
		    print("")
		
		    print("Variables matching [a-z]*")
		    vars = session.BetaGetVariable(
		        "[a-z]*", constants.ENM_WILDCARD
		    )  # returns variables starting with lower letter
		    for key, value in vars.items():
		        p = pickle.loads(value)
		        print("Name: {} Value: {}".format(key, p))
		
		
		if __name__ == "__main__":
		    main()


	"""

def BetaSetVariable(name: str, value: object) -> bool:

	"""

	Ansa script can store user data and address them by a name.
	These data are NOT volatile as script variables and can be accessed either from 
	different scripts or whenever a script is run.
	This function allows the user to store data under a user specified name.

	Parameters
	----------
	name : str
		The name of the beta variable.

	value : object
		A bytes object of the data to store.

	Returns
	-------
	bool
		Returns True on success, or False on failure.

	See Also
	--------
	sdm.session.BetaGetVariable

	Examples
	--------
	::

		import pickle
		
		import sdm
		from sdm import constants
		from sdm import session
		
		
		def main():
		    p = 1
		    v = pickle.dumps(p)
		    session.BetaSetVariable("a", v)
		    v = session.BetaGetVariable("a")
		    p = pickle.loads(v)
		    print(p)
		
		    p = 2
		    v = pickle.dumps(p)
		    session.BetaSetVariable("AB", v)
		
		    print("Variables matching *")
		    vars = session.BetaGetVariable("*", constants.ENM_WILDCARD)  # returns all variables
		    for key, value in vars.items():
		        p = pickle.loads(value)
		        print("Name: {} Value: {}".format(key, p))
		    print("")
		
		    print("Variables matching [a-z]*")
		    vars = session.BetaGetVariable(
		        "[a-z]*", constants.ENM_WILDCARD
		    )  # returns variables starting with lower letter
		    for key, value in vars.items():
		        p = pickle.loads(value)
		        print("Name: {} Value: {}".format(key, p))
		
		
		if __name__ == "__main__":
		    main()


	"""

@typing_extensions.deprecated("Deprecated since version 23.1.0.Use utils.GetProcessSystemMetrics instead.")
def GetMemoryUsage() -> object:

	"""
	.. deprecated:: 23.1.0
		Use :py:func:`utils.GetProcessSystemMetrics` instead.


	Returns the application's physical memory consumption in kilobytes(1024 bytes).

	Returns
	-------
	object
		Returns the application's physical memory consumption on success and None on failure.

	Examples
	--------
	::

		import sdm
		from sdm import session
		
		
		def main():
		    m = session.GetMemoryUsage()
		    print(m)


	"""

	warnings.warn("Deprecated since version 23.1.0.Use utils.GetProcessSystemMetrics instead.", DeprecationWarning)

