from __future__ import annotations
from typing import Iterable, Callable, Any
import warnings
import typing_extensions

NASTRAN: int = None

"""
Defines the NASTRAN Deck.


Examples
--------
::

	import ansa
	from ansa import base
	from ansa import constants
	
	
	def main():
	    ent = base.GetEntity(constants.NASTRAN, "GRID", 1)

"""

LSDYNA: int = None

"""
Defines the LSDYNA Deck.


Examples
--------
::

	import ansa
	from ansa import base
	from ansa import constants
	
	
	def main():
	    ent = base.GetEntity(constants.LSDYNA, "NODE", 1)

"""

PAMCRASH: int = None

"""
Defines the PAMCRASH Deck.


Examples
--------
::

	import ansa
	from ansa import base
	from ansa import constants
	
	
	def main():
	    ent = base.GetEntity(constants.PAMCRASH, "NODE", 1)

"""

ABAQUS: int = None

"""
Defines the ABAQUS Deck.


Examples
--------
::

	import ansa
	from ansa import base
	from ansa import constants
	
	
	def main():
	    ent = base.GetEntity(constants.ABAQUS, "NODE", 1)

"""

RADIOSS: int = None

"""
Defines the RADIOSS Deck.


Examples
--------
::

	import ansa
	from ansa import base
	from ansa import constants
	
	
	def main():
	    ent = base.GetEntity(constants.RADIOSS, "NODE", 1)

"""

ANSYS: int = None

"""
Defines the ANSYS Deck.


Examples
--------
::

	import ansa
	from ansa import base
	from ansa import constants
	
	
	def main():
	    ent = base.GetEntity(constants.ANSYS, "NODE", 1)

"""

PERMAS: int = None

"""
Defines the PERMAS Deck.


Examples
--------
::

	import ansa
	from ansa import base
	from ansa import constants
	
	
	def main():
	    ent = base.GetEntity(constants.ANSYS, "COOR", 1)

"""

FLUENT: int = None

"""
Defines the FLUENT Deck.


Examples
--------
::

	import ansa
	from ansa import base
	from ansa import constants
	
	
	def main():
	    ent = base.GetEntity(constants.FLUENT, "NODE", 1)

"""

FLUENT2D: int = None

"""
Defines the FLUENT2D Deck.


Examples
--------
::

	import ansa
	from ansa import base
	from ansa import constants
	
	
	def main():
	    ent = base.GetEntity(constants.FLUENT2D, "NODE", 1)

"""

STAR: int = None

"""
Defines the STAR Deck.


Examples
--------
::

	import ansa
	from ansa import base
	from ansa import constants
	
	
	def main():
	    ent = base.GetEntity(constants.STAR, "NODE", 1)

"""

UH3D: int = None

"""
Defines the UH3D Deck.


Examples
--------
::

	import ansa
	from ansa import base
	from ansa import constants
	
	
	def main():
	    ent = base.GetEntity(constants.UH3D, "NODE", 1)

"""

CFDPP: int = None

"""
Defines the CFDPP Deck.


Examples
--------
::

	import ansa
	from ansa import base
	from ansa import constants
	
	
	def main():
	    ent = base.GetEntity(constants.CFDPP, "NODE", 1)

"""

OPENFOAM: int = None

"""
Defines the OPENFOAM Deck.


Examples
--------
::

	import ansa
	from ansa import base
	from ansa import constants
	
	
	def main():
	    ent = base.GetEntity(constants.OPENFOAM, "NODE", 1)

"""

MOLDEX3D: int = None

"""
Defines the MOLDEX3D Deck.


Examples
--------
::

	import ansa
	from ansa import base
	from ansa import constants
	
	
	def main():
	    ent = base.GetEntity(constants.MOLDEX3D, "NODE", 1)

"""

RADTHERM: int = None

"""
Defines the RADTHERM Deck.


Examples
--------
::

	import ansa
	from ansa import base
	from ansa import constants
	
	
	def main():
	    ent = base.GetEntity(constants.RADTHERM, "NODE", 1)

"""

SESTRA: int = None

"""
Defines the SESTRA Deck.


Examples
--------
::

	import ansa
	from ansa import base
	from ansa import constants
	
	
	def main():
	    ent = base.GetEntity(constants.SESTRA, "NODE", 1)

"""

THESEUS: int = None

"""
Defines the THESEUS Deck.


Examples
--------
::

	import ansa
	from ansa import base
	from ansa import constants
	
	
	def main():
	    ent = base.GetEntity(constants.THESEUS, "NODE", 1)

"""

app_version: str = None

"""
This function returns the current ansa version.


Examples
--------
::

	import ansa
	from ansa import constants
	
	
	def main():
	    version = constants.app_version
	    print(version)

"""

app_version_int: int = None

"""
This function returns the current ansa version.


Examples
--------
::

	import ansa
	from ansa import constants
	
	
	def main():
	    version = constants.app_version_int
	    print(version)

"""

app_home_dir: str = None

"""
The system directory used for the configuration files.


Examples
--------
::

	import ansa
	from ansa import constants
	
	
	def main():
	    path = constants.app_home_dir
	    print(path)

"""

app_root_dir: str = None

"""
The system's root directory.


Examples
--------
::

	import ansa
	from ansa import constants
	
	
	def main():
	    path = constants.app_root_dir
	    print(path)

"""

FILENAME: str = None

"""
The name of the CAD file currently processed.

"""

FILEPATH: str = None

"""
The directory of the CAD file currently processed.

"""

FLANCH_PROPERTY_ID: int = None

"""
The flanch property ID

"""

PART_COORD_SYS_DX1: float = None

"""
X component of X axis used for Part's transformation.

"""

PART_COORD_SYS_DX2: float = None

"""
X component of Y axis used for Part's transformation.

"""

PART_COORD_SYS_DX3: float = None

"""
X component of Z axis used for Part's transformation.

"""

PART_COORD_SYS_DY1: float = None

"""
Y component of X axis used for Part's transformation.

"""

PART_COORD_SYS_DY2: float = None

"""
Y component of Y axis used for Part's transformation.

"""

PART_COORD_SYS_DY3: float = None

"""
Y component of Z axis used for Part's transformation.

"""

PART_COORD_SYS_DZ1: float = None

"""
Z component of X axis used for Part's transformation.

"""

PART_COORD_SYS_DZ2: float = None

"""
Z component of Y axis used for Part's transformation.

"""

PART_COORD_SYS_DZ3: float = None

"""
Z component of Z axis used for Part's transformation.

"""

PART_COORD_SYS_X: float = None

"""
X coordinate of the origin used for Part's position.

"""

PART_COORD_SYS_Z: float = None

"""
Z coordinate of the origin used for Part's position.

"""

PART_ID: int = None

"""
Module ID of current Part.

"""

PART_MASS: float = None

"""
The Mass of the Part as appears in the Parts Manager.

"""

PART_MATERIAL_ID: int = None

"""
The Material ID that will be assigned to all entities of the Part.

"""

PART_MODEL_NAME: str = None

"""
The PART_MODEL_NAME

"""

PART_NAME: str = None

"""
The name of the Part as appears in the Parts Manager.

"""

PART_VERSION: str = None

"""
The version of the Part as appears in the Parts Manager.

"""

PART_VSC: int = None

"""
The VSC Number of the Part as appears in the Parts Manager.

"""

PART_PROPERTY_ID: int = None

"""
The Property ID that will be assigned to all entities of the Part.

"""

PART_PROPERTY_NAME: str = None

"""
The name of the Property as appears in the Properties list.

"""

PART_PROPERTY_THICKNESS: float = None

"""
The thickness of the Property.

"""

POST_TRANSL_SCRIPT: str = None

"""
.

"""

POST_TRANSL_SCRIPT_ARGS: str = None

"""
.

"""

TRANSLATIONS: int = None

"""
Default character translations, eg. " " = "_", blank space is translated into an underscore.

"""

SEPARATORS: str = None

"""
Definition of whatever is used to separate words, ( eg. , _ . )

"""

MAT_REG: int = None

"""
MAT_REG

"""

SYMMETRY_PART_ID: int = None

"""
SYMMETRY_PART_ID

"""

SYMMETRY_PART_PID_OFFSET: int = None

"""
SYMMETRY_PART_PID_OFFSET

"""

app_temp_dir: str = None

"""
The path of the temporary directory used by the application.


Examples
--------
::

	import ansa
	from ansa import constants
	
	
	def main():
	    path = constants.app_temp_dir
	    print(path)

"""

ENM_REGEX: int = None

"""
A regular expression match (default) for the base.NameToEnts function.

"""

ENM_EXACT: int = None

"""
An exact match for the base.NameToEnts function.

"""

ENM_SUBSTRING: int = None

"""
A sub-string match for the base.NameToEnts function.

"""

ENM_SUBSTRING_IGNORECASE: int = None

"""
A sub-string case-insensitive match for the base.NameToEnts function.

"""

decks: tuple = None

"""
Returns a tuple with all the deck constants. Useful to iterate through all the available decks.


Examples
--------
::

	import ansa
	from ansa import base
	from ansa import constants
	
	
	def main():
	    for deck in constants.decks:
	        print(base.TypesInCategory(deck, "__PROPERTIES__"))

"""

DM_STATUS_UP_TO_DATE: int = None

"""
Defines the "Up to date" value of the "DM Update Status" of an entity


Examples
--------
::

	import ansa
	from ansa import base, constants
	
	
	def getDMUpdateStatus():
	    parts = base.CollectEntities(constants.NASTRAN, None, "ANSAPART")
	    for part in parts:
	        dm_update_status = base.GetEntityDMUpdateStatus(part)
	        if dm_update_status == constants.DM_STATUS_UP_TO_DATE:
	            print('The "' + part._name + '" part has "Up to date" DM Update Status')
	
	
	getDMUpdateStatus()

"""

DM_STATUS_NOT_UP_TO_DATE: int = None

"""
Defines the "Not up to date" value of the "DM Update Status" of an entity


Examples
--------
::

	import ansa
	from ansa import base, constants
	
	
	def getDMUpdateStatus():
	    parts = base.CollectEntities(constants.NASTRAN, None, "ANSAPART")
	    for part in parts:
	        dm_update_status = base.GetEntityDMUpdateStatus(part)
	        if dm_update_status == constants.DM_STATUS_NOT_UP_TO_DATE:
	            print('The "' + part._name + '" part has "Not up to date" DM Update Status')
	
	
	getDMUpdateStatus()

"""

DM_STATUS_MODIFIED: int = None

"""
Defines the "Modified" value of the "DM Update Status" of an entity


Examples
--------
::

	import ansa
	from ansa import base, constants
	
	
	def getDMUpdateStatus():
	    parts = base.CollectEntities(constants.NASTRAN, None, "ANSAPART")
	    for part in parts:
	        dm_update_status = base.GetEntityDMUpdateStatus(part)
	        if dm_update_status == constants.DM_STATUS_MODIFIED:
	            print('The "' + part._name + '" part has "Modified" DM Update Status')
	
	
	getDMUpdateStatus()

"""

DM_STATUS_ALTERNATIVE: int = None

"""
Defines the "Alternative" value of the "DM Update Status" of an entity


Examples
--------
::

	import ansa
	from ansa import base, constants
	
	
	def getDMUpdateStatus():
	    parts = base.CollectEntities(constants.NASTRAN, None, "ANSAPART")
	    for part in parts:
	        dm_update_status = base.GetEntityDMUpdateStatus(part)
	        if dm_update_status == constants.DM_STATUS_ALTERNATIVE:
	            print('The "' + part._name + '" part has "Alternative" DM Update Status')
	
	
	getDMUpdateStatus()

"""

DM_STATUS_NOT_FOUND: int = None

"""
Defines the "Not found" value of the "DM Update Status" of an entity


Examples
--------
::

	import ansa
	from ansa import base, constants
	
	
	def getDMUpdateStatus():
	    parts = base.CollectEntities(constants.NASTRAN, None, "ANSAPART")
	    for part in parts:
	        dm_update_status = base.GetEntityDMUpdateStatus(part)
	        if dm_update_status == constants.DM_STATUS_NOT_FOUND:
	            print('The "' + part._name + '" part was not found in DM')
	
	
	getDMUpdateStatus()

"""

DM_STATUS_ERROR: int = None

"""
Defines the error value when the "DM Update Status" of an entity cannot be identified


Examples
--------
::

	import ansa
	from ansa import base, constants
	
	
	def getDMUpdateStatus():
	    parts = base.CollectEntities(constants.NASTRAN, None, "ANSAPART")
	    for part in parts:
	        dm_update_status = base.GetEntityDMUpdateStatus(part)
	        if dm_update_status == constants.DM_STATUS_ERROR:
	            print("Please add/connect to a DM Root")
	            break
	
	
	getDMUpdateStatus()

"""

REPORT_ALL: int = None

"""
Defines the debug mode to report everything.


Examples
--------
::

	from ansa import base, constants
	
	
	def main():
	    debug_mode = constants.REPORT_ALL
	    fields = {"G1": 15861, "G2": 18709, "G3": 19459}
	    ent, debug_report = base.CreateEntity(
	        constants.ABAQUS, "SHELL", fields, debug=debug_mode
	    )

"""

REPORT_SILENCE: int = None

"""
Defines the debug mode to report silently.


Examples
--------
::

	from ansa import base, constants
	
	
	def main():
	    debug_mode = constants.REPORT_SILENCE
	    fields = {"G1": 15861, "G2": 18709, "G3": 19459}
	    ent, debug_report = base.CreateEntity(
	        constants.ABAQUS, "SHELL", fields, debug=debug_mode
	    )

"""

MARC: int = None

"""
Defines the MARC Deck.


Examples
--------
::

	import ansa
	from ansa import base
	from ansa import constants
	
	
	def main():
	    ent = base.GetEntity(constants.MARC, "NODE", 1)

"""

ACTRAN: int = None

"""
Defines the ACTRAN Deck.


Examples
--------
::

	import ansa
	from ansa import base
	from ansa import constants
	
	
	def main():
	    ent = base.GetEntity(constants.ACTRAN, "NODE", 1)

"""

IMPETUS: int = None

"""
Defines the IMPETUS Deck.


Examples
--------
::

	import ansa
	from ansa import base
	from ansa import constants
	
	
	def main():
	    ent = base.GetEntity(constants.IMPETUS, "NODE", 1)

"""

OPTISTRUCT: int = None

"""
Defines the OPTISTRUCT deck.


Examples
--------
::

	import ansa
	from ansa import base
	from ansa import constants
	
	
	def main():
	    ent = base.GetEntity(constants.OPTISTRUCT, "NODE", 1)

"""

ADVENTURECluster: int = None

"""
Defines the ADVENTURECluster deck.


Examples
--------
::

	import ansa
	from ansa import base
	from ansa import constants
	
	
	def main():
	    ent = base.GetEntity(constants.ADVENTURECluster, "NODE", 1)

"""

