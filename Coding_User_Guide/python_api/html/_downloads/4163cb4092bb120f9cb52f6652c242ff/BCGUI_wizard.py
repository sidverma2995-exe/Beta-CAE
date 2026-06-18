import ansa
from ansa import guitk

def SetLicenseTermsAccepted(cb, state, wizard):

	guitk.BCWizardSetNextButtonEnabled(wizard, state)
	
	return 0

def WizardFinished(wizard, data):
	
	print("Wizard is about to finish (Of course, nothing will be installed)")
	return 1

def WizardCancelled(wizard, data):
	
	print("Wizard is about to cancel.")
	return 1

def wizardCurrentPageChanged(wizard, oldIndex, newIndex, data):
	
	cb = guitk.BCGetUserDataKey(wizard, "acceptCheckBox")
	
	if oldIndex == 0 and newIndex == 1:
		guitk.BCCheckBoxSetChecked(cb, False)
		guitk.BCWizardSetNextButtonEnabled(wizard, False)
	
def CreatePage1(wizard):
	
	page = guitk.BCFrameCreate(wizard)
	guitk.BCBoxLayoutCreate(page, guitk.constants.BCVertical)
	guitk.BCLabelCreate(page, "This wizard will guide you through the installation process.")
	guitk.BCSpacerCreate(page)
	guitk.BCLabelCreate(page, "Please click 'Next' to start.")
	guitk.BCSpacerCreate(page)

	return page

def CreatePage2(wizard):
	
	page = guitk.BCFrameCreate(wizard)
	guitk.BCBoxLayoutCreate(page, guitk.constants.BCVertical)
	guitk.BCLabelCreate(page, "Please read the license carefully.")
	terms = guitk.BCTextEditCreate(page, "Copyright (c) 2011, BETA-CAE Systems")
	guitk.BCTextEditSetReadOnly(terms, True)
	cb = guitk.BCCheckBoxCreate(page, "Accept the license terms")
	guitk.BCSpacerCreate(page)
	
	guitk.BCSetUserDataKey(wizard, "acceptCheckBox", cb)
	guitk.BCCheckBoxSetToggledFunction(cb, SetLicenseTermsAccepted, wizard)
	
	return page

def CreatePage3(wizard):
	
	page = guitk.BCFrameCreate(wizard)
	guitk.BCBoxLayoutCreate(page, guitk.constants.BCVertical)
	guitk.BCLabelCreate(page, "Please click 'Finish' to install the product.")
	guitk.BCSpacerCreate(page)

	return page

def main():
	
	wizard = guitk.BCWizardCreate("Installation Wizard", guitk.constants.BCOnExitDestroy)

	guitk.BCWizardAddPage(wizard, CreatePage1(wizard), "Introduction", "Install BETA-CAE Systems product")
	guitk.BCWizardAddPage(wizard, CreatePage2(wizard), "License", "License Agreement")
	guitk.BCWizardAddPage(wizard, CreatePage3(wizard), "Conclusion", "Ready to Install")
	
	guitk.BCWizardSetCurrentPageChangedFunction(wizard, wizardCurrentPageChanged, None)
	guitk.BCWindowSetAcceptFunction(wizard, WizardFinished, 0)
	guitk.BCWindowSetRejectFunction(wizard, WizardCancelled, 0)

	guitk.BCShow(wizard)
