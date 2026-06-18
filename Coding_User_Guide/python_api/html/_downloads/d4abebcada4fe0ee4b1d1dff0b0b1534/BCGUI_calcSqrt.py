from ansa import guitk
import math

def calculateFun(le, data):
	newVal = math.sqrt(guitk.BCLineEditGetDouble(le))   #Calculation of the square root
	guitk.BCLineEditSetDouble(data, newVal)             #Set calculated value to the output lineEdit
	return 1                                            #Returns 1 so that the window will remain open.

def printFun(button, data):
	textToPrint = 'The calculated value is ' + str(guitk.BCLineEditGetDouble(data))
	print(textToPrint) #Just print the value shown in output lineEdit

def main():
	w = guitk.BCWindowCreate('Sqrt calculation', guitk.constants.BCOnExitDestroy)
	grid = guitk.BCGridLayoutCreate(w, 2, 2)
	
	input = guitk.BCLineEditCreateDouble(grid, 0)
	guitk.BCGridLayoutAddWidget(grid, input, 0, 0, guitk.constants.BCAlignLeft + guitk.constants.BCAlignVCenter)
	
	output = guitk.BCLineEditCreateDouble(grid, 0)
	guitk.BCGridLayoutAddWidget(grid, output, 1, 0, guitk.constants.BCAlignLeft + guitk.constants.BCAlignVCenter)
	guitk.BCLineEditSetReadOnly(output, 1);
	
	guitk.BCLineEditSetEnterPressedFunction(input, calculateFun, output)
	
	butPrint = guitk.BCPushButtonCreate(grid, '', printFun, output)
	guitk.BCButtonSetPixmapFile(butPrint, "print_16.png")
	guitk.BCGridLayoutAddWidget(grid, butPrint, 1, 1, guitk.constants.BCAlignCenter)
	
	guitk.BCLineEditSetMinimumWidth(input, guitk.constants.BCSizeLarge) #Make the LineEdits Large
	guitk.BCLineEditSetMinimumWidth(output, guitk.constants.BCSizeLarge)
	guitk.BCGridLayoutSetColStretch(grid, 0, 1)  #The 1st column should take all
	guitk.BCGridLayoutSetColStretch(grid, 1, 0)  #the expansion.
	guitk.BCDialogButtonBoxCreate(w)
	guitk.BCShow(w)
