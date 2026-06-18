from ansa import base
from ansa import constants        
        
def _exec_func(entities, params):
    pattern = params['Special Character']
    
    # Name of the header in the results/report list
    ck = base.CheckReport(type='Properties with problematic names')
    ck.has_fix = True
    
    for ent in entities:
        if pattern in ent._name:
            ck.add_issue(entities=[ent], status='Error', description='Property name contains a special character', _special_char=pattern, info='Extra column')
    
    return [ck]


def _fix_func(issues):
    for issue in issues:
        for ent in issue.entities:
            name = ent._name
            new_name = name.replace(issue._special_char, '_')
            ent.set_entity_values(constants.NASTRAN, {'Name': new_name})
        
        issue.is_fixed = True
        issue.update()
    
    return base.Check.FIX_APPLIED


def check_prop_names():
    options = {'name': 'Check Property Names', 
               'exec_action': ('_exec_func', __file__), 
               'fix_action': ('_fix_func', __file__), 
               'deck': constants.NASTRAN, 
               'requested_types': ('PSHELL', 'PSOLID' ,'PBEAM'), 
               'info': 'Checks property names'}
    
    my_check = base.CheckDescription(**options) 
    my_check.add_str_param('Special Character', ' ')
    
    return my_check


def main():
    my_check = check_prop_names()
    
    checks_to_save = [my_check]
    base.CheckDescription.save(checks_to_save, '/home/demo/my_checks/my_check.plist')
    
    # obj = base.checks.general.FromDescription(my_check)
    # obj.execute()
