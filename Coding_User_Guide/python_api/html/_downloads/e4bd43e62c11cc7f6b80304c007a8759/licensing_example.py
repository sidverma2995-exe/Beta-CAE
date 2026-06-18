import ansa
from ansa import guitk
from ansa import constants
from ansa import base
from ansa import session

def utilities_tools():
    
    
    ret_feature = session.AcquireFeature('UTILITIES_TOOLS')
    if ret_feature == -12:
        print('No credit is available')
        return 1
    if ret_feature == -10:
        print('This is an invalid feature')
        return 1
    
    _win()
    
    ret = session.ReleaseFeature('UTILITIES_TOOLS')    
    
    print('Done')


def _collect_nodes(direction, dir_value):
    
    nodes = base.CollectEntities(constants.LSDYNA, None, 'NODE')
    
    node_set = base.CreateEntity(constants.LSDYNA, 'SET')
    nodes_to_add = list()
    
    for node in nodes:
        if base.GetEntityCardValues(constants.LSDYNA, node, (direction,))[direction] < dir_value:
            nodes_to_add.append(node)
    
    base.AddToSet(node_set, nodes_to_add)
    
    print('%d nodes were added to set "%d" ' % (len(nodes_to_add), node_set._id))
    

def _check_node_id(node_id):
    
    check = base.GetEntity(constants.LSDYNA, 'NODE', node_id)
    
    if check:
        print('NODE id %d exists' % (node_id,))
    else:
        print('NODE id %d does not exist' % (node_id,))


def _string_replace(str_old, str_new):
    
    props = base.CollectEntities(constants.LSDYNA, None, '__PROPERTIES__')
    counter = 0
    for prop in props:
        new_name = prop._name.replace(str_old, str_new)
        if new_name != prop._name:
            counter += 1
        base.SetEntityCardValues(constants.LSDYNA, prop, {'Name':new_name})
    
    print('Changed name in %d properties' % (counter,))
    

def _ok_pressed(w, data):
    
    if guitk.BCButtonGroupIsChecked(data[0]):
        val = guitk.BCLineEditGetDouble(data[4])
        direction = guitk.BCComboBoxCurrentText(data[3])
        _collect_nodes(direction, val)
    
    if guitk.BCButtonGroupIsChecked(data[1]):
        node_id = guitk.BCLineEditGetInt(data[5])
        _check_node_id(node_id)
    
    if guitk.BCButtonGroupIsChecked(data[2]):
        str_old = guitk.BCLineEditGetText(data[6])
        str_new = guitk.BCLineEditGetText(data[7])
        _string_replace(str_old, str_new)
        
    
    guitk.BCDestroyLater(w)
    return True

def _cancel_pressed(w, data):
    
    guitk.BCDestroyLater(w)
    return False

def _win():
    
    CVals_5 = ('X', 'Y', 'Z')
    TopWindow = guitk.BCWindowCreate("TopWindow", guitk.constants.BCOnExitDestroy)
    BCTabWidget_1 = guitk.BCTabWidgetCreate(TopWindow)
    BCFrame_1 = guitk.BCFrameCreate(BCTabWidget_1)
    BCFrame_2 = guitk.BCFrameCreate(BCTabWidget_1)
    BCBoxLayout_1 = guitk.BCBoxLayoutCreate(BCFrame_1, guitk.constants.BCVertical)
    BCBoxLayout_2 = guitk.BCBoxLayoutCreate(BCFrame_2, guitk.constants.BCVertical)
    BCButtonGroup_1 = guitk.BCButtonGroupCreate(BCBoxLayout_1, "Find nodes based on location", guitk.constants.BCVertical)
    BCHBox_1 = guitk.BCHBoxCreate(BCButtonGroup_1)
    BCComboBox_1 = guitk.BCComboBoxCreate(BCHBox_1, CVals_5)
    BCLabel_1 = guitk.BCLabelCreate(BCHBox_1, "<")
    BCLineEdit_1 = guitk.BCLineEditCreateDouble(BCHBox_1, 0.0000000000)
    BCSpacer_1 = guitk.BCSpacerCreate(BCHBox_1)
    BCButtonGroup_2 = guitk.BCButtonGroupCreate(BCBoxLayout_1, "Check if node exists by id", guitk.constants.BCVertical)
    BCHBox_2 = guitk.BCHBoxCreate(BCButtonGroup_2)
    BCLabel_2 = guitk.BCLabelCreate(BCHBox_2, "id")
    BCLineEdit_2 = guitk.BCLineEditCreateInt(BCHBox_2, 0)
    BCSpacer_2 = guitk.BCSpacerCreate(BCHBox_2)
    guitk.BCLineEditSetMaxLength(BCLineEdit_2, 20)
    BCButtonGroup_3 = guitk.BCButtonGroupCreate(BCBoxLayout_1, "Find and replace in property name", guitk.constants.BCVertical)
    BCHBox_3 = guitk.BCHBoxCreate(BCButtonGroup_3)
    BCLabel_3 = guitk.BCLabelCreate(BCHBox_3, "Find")
    BCLineEdit_3 = guitk.BCLineEditCreate(BCHBox_3, "")
    BCLabel_4 = guitk.BCLabelCreate(BCHBox_3, "Replace by")
    BCLineEdit_4 = guitk.BCLineEditCreate(BCHBox_3, "")
    BCSpacer_3 = guitk.BCSpacerCreate(BCHBox_3)
    BCDialogButtonBox_1 = guitk.BCDialogButtonBoxCreate(BCBoxLayout_1)
    guitk.BCButtonGroupSetCheckable(BCButtonGroup_1, 1)
    guitk.BCComboBoxSetSizeLimit(BCComboBox_1, 5)
    guitk.BCSpacerChangeSize(BCSpacer_1, 300, 2, guitk.constants.BCExpanding, guitk.constants.BCExpanding)
    guitk.BCSpacerChangeSize(BCSpacer_2, 500, 2, guitk.constants.BCExpanding, guitk.constants.BCExpanding)
    guitk.BCSpacerChangeSize(BCSpacer_3, 200, 2, guitk.constants.BCExpanding, guitk.constants.BCExpanding)
    guitk.BCButtonGroupSetCheckable(BCButtonGroup_2, 1)
    guitk.BCButtonGroupSetCheckable(BCButtonGroup_3, 1)
    guitk.BCTabWidgetAddTab(BCTabWidget_1, BCFrame_1, "Tools")
    guitk.BCTabWidgetAddTab(BCTabWidget_1, BCFrame_2, "About")
    current_tab = guitk.BCTabWidgetGetTab(BCTabWidget_1, 0)
    guitk.BCTabWidgetSetCurrentTab(BCTabWidget_1, current_tab)
    
    BCLabel_5 = guitk.BCLabelCreate(BCBoxLayout_2, "Title: Utilities Tools \nDeveloper: BETA CAE Systems\nVersion: 1.0.0 \nReleased Date: 01/09/2015")
    BCSpacer_4 = guitk.BCSpacerCreate(BCBoxLayout_2)
    guitk.BCSpacerChangeSize(BCSpacer_4, 2, 300, guitk.constants.BCExpanding, guitk.constants.BCExpanding)
    data = (BCButtonGroup_1, BCButtonGroup_2, BCButtonGroup_3, BCComboBox_1, BCLineEdit_1, BCLineEdit_2, BCLineEdit_3, BCLineEdit_4)
    
    guitk.BCWindowSetAcceptFunction(TopWindow, _ok_pressed, data)
    guitk.BCWindowSetRejectFunction(TopWindow, _cancel_pressed, None)
    guitk.BCShow(TopWindow)


