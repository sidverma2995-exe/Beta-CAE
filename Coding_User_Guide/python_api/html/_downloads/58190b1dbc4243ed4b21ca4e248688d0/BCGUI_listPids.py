import ansa
from ansa import guitk
from ansa import constants
from ansa import base
from ansa import session

#Column numbers declaration
COL_NUMS = 7
CHECK_COL = 0
COLOR_COL = 1
PID_COL = 2
NAME_COL = 3
ELEMS_COL = 4
MID_COL = 5
FROZEN_COL = 6

LINE_EDIT_PATH_ID = 0
PROGRESS_BAR_ID = 1

def checkButtonPressedFun(item, state, data):

	search_type = ("FACE", "SHELL")
	pshell = guitk.BCListViewItemGetUserData(item)
	shells = base.CollectEntities(constants.NASTRAN, pshell, search_type, True)
	#change the visibility of the shells
	if state:
		base.And(pshell)
	else:
		base.Not(pshell)
	#If the property has non-visible elements, uncheck button
	if state and not len(shells):
		guitk.BCListViewItemCheckableSetOn(item, False)

def renameFun(item, column, list_bc):
	pshell = guitk.BCListViewItemGetUserData(item);

	if column == NAME_COL:  #Renaming PSHELL's Name
		newName = guitk.BCListViewItemGetText(item, NAME_COL)
		base.SetEntityCardValues(constants.NASTRAN, pshell, {"Name":newName})
	
	elif column == MID_COL:    #Resetting PSHELL's MID
		newMID = guitk.BCListViewItemGetInt(item, MID_COL)
		mats = base.CollectEntities(constants.NASTRAN, None, "MAT1", False)
		i = 0
		ids = []
		for mat in mats:
			ids.append(mat._id)
			#Check if user inputed MID exists
			if newMID in ids:
				base.SetEntityCardValues(constants.NASTRAN, pshell, {"MID1": newMID})
			else:
				ret = base.GetEntityCardValues(constants.NASTRAN, pshell, ("MID1",))
				guitk.BCListViewItemSetText(item, MID_COL, str(ret['MID1']))
				info_box = guitk.BCGetUserDataKey(list_bc, 'info_box')
				#Check if the user typed text or number
				if newMID < guitk.constants.blank:
					guitk.BCItemViewInfoBoxSetText(info_box, 0, "No material with id "+str(newMID)+" exists!")
				else:
					guitk.BCItemViewInfoBoxSetText(info_box, 0, "The material id must be an integer!")

def updateItem(list_bc, item):

	search_type = ("FACE", "SHELL")
	pshell = guitk.BCListViewItemGetUserData(item)
	ret = base.GetEntityCardValues(constants.NASTRAN, pshell, ("PID", "MID1", "Name", "FROZEN_ID", "COLOR_R", "COLOR_B", "COLOR_G"))

	shells = base.CollectEntities(constants.NASTRAN, pshell, search_type, True)
	num = len(shells)
	v = 0
	for ent in shells:
		if  base.IsEntityVisible(ent):
			v = 1
			break

	guitk.BCListViewItemCheckableSetOn(item, v)
	guitk.BCListViewItemSetRectangleColor(item, COLOR_COL, ret['COLOR_R'], ret['COLOR_G'], ret['COLOR_B'])
	guitk.BCListViewItemSetText(item, PID_COL, str(ret['PID']))
	guitk.BCListViewItemSetText(item, NAME_COL, ret['Name'])
	guitk.BCListViewItemSetText(item, ELEMS_COL, str(num))
	guitk.BCListViewItemSetText(item, MID_COL, str(ret['MID1']))
	guitk.BCListViewItemSetText(item, FROZEN_COL, ret['FROZEN_ID'])
	guitk.BCListViewFilterUpdateComboBox(list_bc, FROZEN_COL)

def destroyItem(item):

	#Just delete the item, not the PSHELL itself.
	guitk.BCListViewItemDestroy(item)
	return 0

def mouseClickFun(list_bc, mb, item, col, data):

	if not item:
		return 0

	if mb == guitk.constants.BCRightButton:
		guitk.BCTimerSingleShot(0, destroyItem, item)
	return 0

def doubleClickFun(list_bc, item, col, data):

	if not item:
		return 1

	pshell = guitk.BCListViewItemGetUserData(item)
	base.EditEntity(constants.NASTRAN, pshell)
	updateItem(list_bc, item)       #Update item after a possible editing.
	return 1

def updateList(list_bc):

	guitk.BCListViewClear(list_bc)
        
	ws = guitk.BCGetUserDataKey(list_bc, 'ws')
	pb = guitk.BCWidgetStackWidget(ws, PROGRESS_BAR_ID) #Getting the BCProgressBar with its id
	guitk.BCWidgetStackRaiseId(ws, PROGRESS_BAR_ID)
	guitk.BCProgressBarSetProgress(pb, 0)

	search_type = ("PSHELL",)
	pshells = base.CollectEntities(constants.NASTRAN, None, search_type, False)
	guitk.BCProgressBarSetTotalSteps(pb, len(pshells))

	search_type = ("FACE", "SHELL")
	rename = (0, 0, 0, 3, 0, 2, 0)

	for pshell in pshells:
		shells = base.CollectEntities(constants.NASTRAN, pshell, search_type, True)
		num = len(shells)
		ret = base.GetEntityCardValues(constants.NASTRAN, pshell, ("PID", "MID1", "Name", "FROZEN_ID", "COLOR_R", "COLOR_G", "COLOR_B"))
		titles = ["", "", str(ret['PID']), ret['Name'], str(num), str(ret['MID1']), ret['FROZEN_ID']]
		
		item = guitk.BCListViewAddItem(list_bc, COL_NUMS, titles, rename)
		guitk.BCListViewItemSetUserData(item, pshell)
		guitk.BCListViewItemSetRectangleColor(item, COLOR_COL, ret['COLOR_R'], ret['COLOR_G'], ret['COLOR_B'])
		guitk.BCListViewItemSetRenamedFunction(item, renameFun, list_bc)

		#Check if current pshell is visible
		v = False
		if base.IsEntityVisible(pshell):
			v=True
			
		guitk.BCListViewItemSetCheckable(item, True)
		guitk.BCListViewItemCheckableSetOn(item, v)
		guitk.BCListViewItemCheckableSetToggledFunction(item, checkButtonPressedFun, None)
		
		#Update progressBar
		current = guitk.BCProgressBarProgress(pb)
		guitk.BCProgressBarSetProgress(pb, current+1)

	guitk.BCListViewFilterUpdateComboBox(list_bc, FROZEN_COL)
	guitk.BCWidgetStackRaiseId(ws, LINE_EDIT_PATH_ID)

def onEnterFun(le, list_bc):
	#Open file and update list
	my_file = guitk.BCLineEditGetText(le)
	print(my_file)
	
	if my_file != base.DataBaseName():
		session.New('blank')
		base.Open(my_file)
	updateList(list_bc)
	return 1

def clearListFun(b, list_bc):
	guitk.BCListViewClear(list_bc)

def main():
	titles = ("Visible", "Color", "PID", "Name", "Elements", "MID1", "FROZEN_ID")

	base.SetCurrentDeck(constants.NASTRAN)
	w = guitk.BCWindowCreate("PIDs list", guitk.constants.BCOnExitDestroy)
        
	#Create a splitter between the two widgets
	spl = guitk.BCSplitterCreate(w, guitk.constants.BCVertical)
        
	#Create a widgetStack to place a BCLineEditPath and a BCProgressBar
	ws = guitk.BCWidgetStackCreate(spl)
	lep = guitk.BCLineEditPathCreate(w, 1, base.DataBaseName(), 0, "ANSA_Example_lineEditPath")
	guitk.BCWidgetStackAddWidget(ws, lep, LINE_EDIT_PATH_ID)
	pb = guitk.BCProgressBarCreate(ws, 0)
	guitk.BCWidgetStackAddWidget(ws, pb, PROGRESS_BAR_ID)
	guitk.BCWidgetStackRaiseWidget(ws, lep);

	#The list will be controlled by BCWidgetExpand we
	we = guitk.BCWidgetExpandCreate(spl);
	list_bc = guitk.BCListViewCreate(we, COL_NUMS, titles, 1)
	guitk.BCWidgetExpandSetWidget(we, list_bc)

	#Setting BCLineEditPath
	combo = guitk.BCLineEditPathGetCombo(lep)
	le = guitk.BCComboBoxGetLineEdit(combo)

	guitk.BCLineEditSetExtentionsFilter(le, ["ansa"])

	#The file selected by file manager will update the list, as well
	guitk.BCLineEditPathSetDialogEnterEnabled(lep, 1)
	guitk.BCLineEditPathSetEnterPressedFunction(lep, onEnterFun, list_bc)

	#Set the alignment of data shown in each column.
	guitk.BCListViewSetColumnAlignment(list_bc, PID_COL, guitk.constants.BCAlignRight)
	guitk.BCListViewSetColumnAlignment(list_bc, ELEMS_COL, guitk.constants.BCAlignRight)
	guitk.BCListViewSetColumnAlignment(list_bc, MID_COL, guitk.constants.BCAlignRight)
	guitk.BCListViewSetColumnAlignment(list_bc, FROZEN_COL, guitk.constants.BCAlignCenter)

	#Set the multi condition filter.
	guitk.BCListViewSetFilterEnabled(list_bc, True)
	guitk.BCListViewSetColumnDataTypes(list_bc, (guitk.constants.BCBool, guitk.constants.BCInvalid, guitk.constants.BCInt, guitk.constants.BCString, guitk.constants.BCInt, guitk.constants.BCInt, guitk.constants.BCBool))
	guitk.BCListViewFilterSetColumnEnabled(list_bc, CHECK_COL, 0)
	guitk.BCListViewFilterSetColumnEnabled(list_bc, COLOR_COL, 0)
	guitk.BCListViewFilterSetComboBox(list_bc, FROZEN_COL)

	#Set a BCItemViewInfoBox
	info_box = guitk.BCItemViewInfoBoxCreate(w, list_bc)
	guitk.BCSetUserDataKey(list_bc, "info_box", info_box)
	
	#Set a double click function and a right click function
	guitk.BCListViewSetDoubleClickedFunction(list_bc, doubleClickFun, 0)
	guitk.BCListViewSetMouseClickedFunction(list_bc, mouseClickFun, 0)

	guitk.BCSetUserDataKey(list_bc, "ws", ws)      #We will need ws in updateList
	updateList(list_bc)

	ddb = guitk.BCDialogButtonBoxCreate(w)
	clear = guitk.BCPushButtonCreate(ddb, "Clear list", clearListFun, list_bc)
	guitk.BCDialogButtonBoxAddButton(ddb, clear)

	guitk.BCShow(w)
        
main()
