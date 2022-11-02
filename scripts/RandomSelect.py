"""
Randomly select objects.
"""

import random
import maya.cmds as cmds

amount_to_divide = 2

sel = cmds.ls(selection=True)
selection_children = cmds.listRelatives(sel, ad=True)

obj_list = []
for obj in selection_children:
	if "Shape" not in obj:
		obj_list.append(obj)

count_objects = len(obj_list)
amount_to_select = count_objects / amount_to_divide

chosen_list = []
for i in range(int(amount_to_select)):
    chosen = random.choice(obj_list)
    chosen_list.append(chosen)
    
cmds.select(chosen_list)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	




