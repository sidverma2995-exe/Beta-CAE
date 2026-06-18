import ansa
from ansa import guitk
from ansa import constants

def tabChangedFun(tw, oldTab, newTab, window): 
	readOnDemand = guitk.BCGetUserDataKey(window, "readOnDemand")
	saveOnDemand = guitk.BCGetUserDataKey(window, "saveOnDemand")
	tab1 = guitk.BCGetUserDataKey(window, "tab1")
	if tab1 == newTab:
		e = True
	else:
		e = False
	#Disable read and save button for second tab, since they are not applicable
	guitk.BCSetEnabled(readOnDemand, e)
	guitk.BCSetEnabled(saveOnDemand, e)
	
	guitk.BCSetCaption(window, guitk.BCTabWidgetGetTabLabel(tw, newTab))
	return 0
	
def radioButtonPressed(bgroup, index, data):
	print("Radio Button Pressed: " + str(index+1))

def comboBoxChanged(combo, index, popup):
	if index == 2:
		print(index)
		guitk.BCPopupMenuPopup(popup)
	
def checkWindow(w, data):
	spin = guitk.BCGetUserDataKey(w, "spin")
	if guitk.BCSpinBoxGetInt(spin) > 6:
		guitk.BCWindowFlash(w) #That's a flashy feature...
		return "The spin box value is too high!"
	return ""

def readSettingsOnDemand(b, window):
	guitk.BCWindowReadControlSettings(window)

def saveSettingsOnDemand(b, window):
	guitk.BCWindowSaveControlSettings(window)
	
def createToolBox(window, BCVBox_1):
	BCLabel_1 = guitk.BCLabelCreate(BCVBox_1, "Common Widgets")
	BCToolBox_1 = guitk.BCToolBoxCreate(BCVBox_1)
	blueFrame = guitk.BCFrameCreate(BCToolBox_1)
	BCBoxLayout_1 = guitk.BCBoxLayoutCreate(blueFrame, guitk.constants.BCVertical)
	redFrame = guitk.BCFrameCreate(BCToolBox_1)
	BCBoxLayout_2 = guitk.BCBoxLayoutCreate(redFrame, guitk.constants.BCHorizontal)
	greenFrame = guitk.BCFrameCreate(BCToolBox_1)
	BCBoxLayout_3 = guitk.BCBoxLayoutCreate(greenFrame, guitk.constants.BCHorizontal)
	guitk.BCToolBoxInsertItem(BCToolBox_1, blueFrame, "Blue Frame", -1)
	guitk.BCToolBoxInsertItem(BCToolBox_1, redFrame, "Red Frame", -1)
	guitk.BCToolBoxInsertItem(BCToolBox_1, greenFrame, "Green Frame", -1)
	guitk.BCSetBackgroundColor(blueFrame, 100, 100, 255)
	guitk.BCSetBackgroundColor(redFrame, 255, 100, 100)
	guitk.BCSetBackgroundColor(greenFrame, 100, 255, 100)
	
	#BLUE FRAME
	#create a drawer
	drawer = guitk.BCDrawerGridCreate(blueFrame)
	
	#create 3 check boxes
	checkFrame = guitk.BCFrameCreate(drawer)
	guitk.BCBoxLayoutCreate(checkFrame, guitk.constants.BCHorizontal)
	checkBoxA = guitk.BCCheckBoxCreate(checkFrame, "CheckBox A")
	checkBoxB = guitk.BCCheckBoxCreate(checkFrame, "CheckBox B")
	checkBoxC = guitk.BCCheckBoxCreate(checkFrame, "CheckBox C")
	
	#create a button group with radio buttons
	bgroup = guitk.BCButtonGroupCreate(drawer, "Exclusive Radios", guitk.constants.BCVertical)
	guitk.BCButtonGroupSetCheckable(bgroup, 1)
	for i in range(4):
		name = "RadioButton " + str(i+1)
		rb = guitk.BCRadioButtonCreate(bgroup, name, None, None)
	guitk.BCButtonGroupSetPressedFunction(bgroup, radioButtonPressed, None)
	
	#create a button
	buttonFrame = guitk.BCFrameCreate(drawer)
	guitk.BCBoxLayoutCreate(buttonFrame, guitk.constants.BCHorizontal)
	toggleButton1 = guitk.BCPushButtonCreate(buttonFrame, "toggleButton1", None, None)
	guitk.BCRadioButtonAddManagedWidget(rb, toggleButton1, guitk.constants.BCManagedShow, guitk.constants.BCManagedHide)
	toggleButton2 = guitk.BCToolButtonCreate(buttonFrame, "filter_16.png", "toggleButton2", None, None)
	guitk.BCButtonSetToggleButton(toggleButton1, 1)
	
	#add the widgets to the drawer
	guitk.BCDrawerGridInsertWidget(drawer, checkFrame, 1, "CheckBoxes")
	guitk.BCDrawerGridInsertStableWidget(drawer, bgroup)
	guitk.BCDrawerGridInsertWidget(drawer, buttonFrame, 1, "Buttons")
	
	#RED FRAME
	guitk.BCLabelCreate(redFrame, "Degrees:")
	spin = guitk.BCSpinBoxCreate(redFrame)
	guitk.BCSetUserDataKey(window, 'spin', spin) #We will need this for the 'checkWIndow' function
	
	#GREEN FRAME
	comboBox = guitk.BCComboBoxCreate(greenFrame, ['All', 'None', 'Write Protected'])
		
	#create a popupmenu
	popup = guitk.BCPopupMenuCreate(comboBox)
	popupFrame = guitk.BCFrameCreate(popup)
	popupVbox = guitk.BCBoxLayoutCreate(popupFrame, guitk.constants.BCVertical)
	guitk.BCBoxLayoutSetMargin(popupVbox, 0)
	guitk.BCBoxLayoutSetSpacing(popupVbox, 0)
	lview = guitk.BCListViewCreate(popupVbox, 1, ("",), True)
	guitk.BCListViewSetResizeMode(lview, guitk.constants.BCLastColumn)
	guitk.BCListViewHeaderSetVisible(lview, 0)
	guitk.BCListViewSetIsRootDecorated(lview, 1)
	guitk.BCListViewSetSelectionMode(lview, guitk.constants.BCMulti)
	guitk.BCListViewSetSortingColumn(lview, 0, 1)
	for i in range(8):
		lvitem = guitk.BCListViewAddItem(lview, 1, ('tmpItem',), (0,))
	
	ok_but = guitk.BCPushButtonCreate(popupVbox, "OK", None, None)

	guitk.BCPopupMenuInsertWidget(popup, popupFrame)
		
	#The callback function
	guitk.BCComboBoxSetActivatedFunction(comboBox, comboBoxChanged, popup)
  
def createSecondTab(window, BCVBox_2):
	#Create the line edit and the button
	BCHBOX_1 = guitk.BCHBoxCreate(BCVBox_2)
	le = guitk.BCLineEditCreate(BCHBOX_1, '')
	guitk.BCPushButtonCreate(BCHBOX_1, 'OK', None, None)
	#Create the grid with the buttons
	grid = guitk.BCGridLayoutCreate(BCVBox_2, 3, 3)
	for i in range(3):
		for j in range(3):
			button = guitk.BCPushButtonCreate(grid, 'Button_' + str(i) + '_' + str(j), None, None)
			guitk.BCGridLayoutAddWidget(grid, button, i, j, guitk.constants.BCAlignVCenter + guitk.constants.BCAlignLeft)
	#Create a text edit
	guitk.BCTextEditCreate(BCVBox_2, '')
	#Create a label ticker
	guitk.BCLabelTickerCreate(BCVBox_2, 'BCTicker has the ability to scroll from left to right, when the text does not fit in the window.')
	
def main():
	window = guitk.BCWindowCreate("Auto Saving Settings", guitk.constants.BCOnExitDestroy)
	#Check on enter
	guitk.BCWindowSetCheckFunction(window, checkWindow, None)
	
	BCTabWidget_1 = guitk.BCTabWidgetCreate(window)
	
	#Create the first tab
	BCVBox_1 = guitk.BCVBoxCreate(BCTabWidget_1)
	createToolBox(window, BCVBox_1)
	
	#Create the second tab
	BCVBox_2 = guitk.BCVBoxCreate(BCTabWidget_1)
	createSecondTab(window, BCVBox_2)
	
	#Insert the Tabs
	guitk.BCTabWidgetInsertTab(BCTabWidget_1, BCVBox_1, "Tool Box", -1)
	guitk.BCTabWidgetInsertTab(BCTabWidget_1, BCVBox_2, "Buttons and BCLineEdit", -1)
	guitk.BCTabWidgetSetTabMovingEnabled(BCTabWidget_1, True)
	guitk.BCTabWidgetSetCurrentTab(BCTabWidget_1, BCVBox_1)
	guitk.BCSetCaption(window, 'Tool Box')
	
	#Create a BCDialogButtonBox with the 2 extra buttons
	dbb = guitk.BCDialogButtonBoxCreate(window)
	readOnDemand = guitk.BCPushButtonCreate(dbb, "Read On Demand", readSettingsOnDemand, window);
	saveOnDemand = guitk.BCPushButtonCreate(dbb, "Save On Demand", saveSettingsOnDemand, window)
	guitk.BCDialogButtonBoxAddButton(dbb, readOnDemand)
	guitk.BCDialogButtonBoxAddButton(dbb, saveOnDemand)
	
	guitk.BCSetUserDataKey(window, 'readOnDemand', readOnDemand)
	guitk.BCSetUserDataKey(window, 'saveOnDemand', saveOnDemand)
	guitk.BCSetUserDataKey(window, 'tab1', BCVBox_1)
	guitk.BCTabWidgetSetCurrentChangedFunction(BCTabWidget_1, tabChangedFun, window)
	guitk.BCShow(window)

main()
