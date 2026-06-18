from ansa import guitk
import math

def calculateEquation(data): #Retrieving widgets from BCWindow w (==data)
	input = guitk.BCGetUserDataKey(data, "input")
	sp1 = guitk.BCGetUserDataKey(data, "sp1")
	sp2 = guitk.BCGetUserDataKey(data, "sp2")

	#Calculation
	d = guitk.BCLineEditGetDouble(input)
	if d <= 0 or d == 1:
		result = None
	else:
		i_1 = guitk.BCSpinBoxGetInt(sp1)
		i_2 = guitk.BCSpinBoxGetInt(sp2)
		result = math.pow(d, i_1) * math.exp(i_2) / math.log10(d)
	guitk.BCSetUserDataKey(data, "result", result)

def lineEditChangedFun(le, text, data):
	#le is the input lineEdit; data is the w BCWindow
	lab = guitk.BCGetUserDataKey(data, "lab")
	d = guitk.BCLineEditGetDouble(le)
	if d == guitk.constants.blank: #if the input field is blank
		d = 0.0
	guitk.BCLabelSetText(lab, str(d))
        
	calculateEquation(data)
	return 0

def spinBoxChangedFun(sp, val, data):
	#sp here could be sp1 or sp2 BCSpinBoxes; data is the w BCWindow
	calculateEquation(data)
	return 0

def printFun(button, data):
	#button here is butPrint; data is the w BCWindow
	#Just print the value shown in output lineEdit
	input = guitk.BCGetUserDataKey(data, "input")
	output = guitk.BCGetUserDataKey(data, "output")
	lab = guitk.BCGetUserDataKey(data, "lab")
	result = guitk.BCGetUserDataKey(data, "result")
        
	d = str(guitk.BCLineEditGetDouble(input))
	if result is None:
		guitk.BCLineEditSetDouble(output, guitk.constants.blank)#Give blank as output
		textToPrint = "The input value cannot be negative or 1"
	else:
		guitk.BCLineEditSetDouble(output, result)
		textToPrint = "The calculated value is " + str(result)
	print(textToPrint)

def main():
	w = guitk.BCWindowCreate("Equation calculation", guitk.constants.BCOnExitDestroy)
	l1 = guitk.BCBoxLayoutCreate(w, guitk.constants.BCHorizontal)
	input = guitk.BCLineEditCreateDouble(l1, 1)
	guitk.BCLabelCreate(l1, " ^ ")
	sp1 = guitk.BCSpinBoxCreate(l1)
	guitk.BCSpinBoxSetMinValue(sp1, 2)
	guitk.BCSpinBoxSetMaxValue(sp1, 15)
	guitk.BCLabelCreate(l1, " * e ^ ")
	sp2 = guitk.BCSpinBoxCreate(l1)
	guitk.BCSpinBoxSetMinValue(sp2, 1)
	guitk.BCSpinBoxSetMaxValue(sp2, 10)
	guitk.BCLabelCreate(l1, " / log(")
	lab = guitk.BCLabelCreate(l1, guitk.BCLineEditGetText(input))
	guitk.BCLabelCreate(l1, ")")
	guitk.BCSpacerCreate(w)
	l2 = guitk.BCBoxLayoutCreate(w, guitk.constants.BCHorizontal)
	output = guitk.BCLineEditCreateDouble(l2, 0)
	guitk.BCLineEditSetReadOnly(output, 1)
	butPrint = guitk.BCPushButtonCreate(l2, '', printFun, w) #You can also set the widget before the data assignment
	guitk.BCButtonSetPixmapFile(butPrint, "print_16.png")
	guitk.BCSpacerCreate(l2) #Horizontal spacer. Keeps output and butPrint to the left

	guitk.BCSetUserDataKey(w, "input", input)
	guitk.BCSetUserDataKey(w, "sp1", sp1)
	guitk.BCSetUserDataKey(w, "sp2", sp2)
	guitk.BCSetUserDataKey(w, "lab", lab)#We hold the lab in order to change its text.
	guitk.BCSetUserDataKey(w, "output", output)
	guitk.BCSetUserDataKey(w, "result", None)#create a variable to hold the result

	guitk.BCSpinBoxSetValueChangedFunction(sp1, spinBoxChangedFun, w)
	guitk.BCSpinBoxSetValueChangedFunction(sp2, spinBoxChangedFun, w)
	guitk.BCLineEditSetTextChangeFunction(input, lineEditChangedFun, w)

	guitk.BCDialogButtonBoxCreate(w)
	guitk.BCShow(w)


