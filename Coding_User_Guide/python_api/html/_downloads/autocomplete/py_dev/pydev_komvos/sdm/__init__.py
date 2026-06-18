from __future__ import annotations
from typing import Iterable, Callable, Any
import warnings
import typing_extensions
from . import constants, guitk, base, sdm_base, dm, utils, session, spdrm, script, betascript, ml
from types import ModuleType

def ImportCode(path: str) -> int:

	"""

	This function imports the code from another python module (py or pyb).

	Parameters
	----------
	path : str
		The name of the script file to import.

	Returns
	-------
	int
		Returns 0 on success, else an exception is raised.

	Raises
	------
	FileNotFoundError
		Cannot read the file.

	Notes
	-----
	If you want to import Python modules (.py), it is recommended to use the native Python mechanism.
	This function should ideally be used only for importing Beta encrypted Python modules (.pyb).
	Notice, that in this case, you don't have to add the filepath in python system path.

	Examples
	--------
	::

		import sdm
		
		file1 = "/home/demo/module1.pyb"
		file2 = "C:\\\\demo\\\\module2.pyb"
		
		sdm.ImportCode(file1)
		sdm.ImportCode(file2.replace("\\\\", "/"))
		
		
		def main():
		    module1.function1()
		    module2.function1()


	"""

def ScriptCurrentDir() -> str:

	"""

	Returns the current working directory path.

	Returns
	-------
	str
		Returns the current working directory.

	See Also
	--------
	sdm.ScriptHomeDir, sdm.ScriptUserDir

	Examples
	--------
	::

		import sdm
		
		
		def main():
		    print(sdm.ScriptCurrentDir())


	"""

@typing_extensions.deprecated("Deprecated.Use ansa.constants.app_root_dir instead.")
def ScriptHomeDir() -> str:

	"""
	.. deprecated::
		Use :py:const:`ansa.constants.app_root_dir` instead.


	Returns the ANSA/META Home directory path

	Returns
	-------
	str
		Returns the ANSA/META Home directory path.

	See Also
	--------
	sdm.ScriptCurrentDir, sdm.ScriptUserDir

	Examples
	--------
	::

		import sdm
		
		
		def main():
		    print(sdm.ScriptHomeDir())


	"""

	warnings.warn("Deprecated.Use ansa.constants.app_root_dir instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated.Use ansa.constants.app_home_dir instead.")
def ScriptUserDir() -> str:

	"""
	.. deprecated::
		Use :py:const:`ansa.constants.app_home_dir` instead.


	Returns the BetaHome directory path.

	Returns
	-------
	str
		Returns the BetaHome directory path.

	See Also
	--------
	sdm.ScriptCurrentDir, sdm.ScriptHomeDir

	Examples
	--------
	::

		import sdm
		
		
		def main():
		    print(sdm.ScriptUserDir())


	"""

	warnings.warn("Deprecated.Use ansa.constants.app_home_dir instead.", DeprecationWarning)

def CompileScript(fileInput: str, fileOutput: str, moduleName: str, mode: bool=True) -> int:

	"""

	Creates a compiled (pyb/bsx) file from the given script path.

	Parameters
	----------
	fileInput : str
		The path of the script that we want to compile.

	fileOutput : str
		The destination path of the created compiled file.

	moduleName : str
		The name of the module.

	mode : bool, optional
		Declares whether to include the input script's imported modules, inside the final compiled file.
		(Applicable to all the imported modules, either through the native Python "import", or through the "ansa.ImportCode" function)
		-True, to include dependencies in the compiled script. (Default)
		-False, otherwise.
		It has effect only for Python scripts.

	Returns
	-------
	int
		Returns 1 on success, 0 on failure.

	Examples
	--------
	::

		import sdm
		
		
		def main():
		    sdm.CompileScript(
		        "/home/user/scripts/some_script.py",
		        "/home/user/scripts/some_script.pyb",
		        "moduleName",
		    )
		
		
		if __name__ == "__main__":
		    main()


	"""

def PybImport(module_name: str, script_file_path: str) -> ModuleType:

	"""

	A function that imports python scripts (pyb).
	Returns the imported module.

	Parameters
	----------
	module_name : str
		The name of the module.

	script_file_path : str
		The filepath of the script.

	Returns
	-------
	ModuleType
		Returns the imported module.

	Examples
	--------
	::

		import sdm
		
		
		def main():
		    x = sdm.PybImport("moduleName", "/module/file/path/moduleNameCompiled.pyb")
		    x.funcInModuleNameCompiled()


	"""

def ReadingFile() -> str:

	"""

	Function that returns the currently reading physical file on disk.

	Returns
	-------
	str
		Returns the currently reading physical file on disk.

	Examples
	--------
	::

		import sdm
		
		
		def main():
		    x = sdm.ReadingFile()
		    print(x)


	"""

