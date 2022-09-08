""" Combine curve shapes """

import maya.cmds as cmds


selection = cmds.ls(selection=True)[0]
selection_children = cmds.listRelatives(selection, ad=True) # shape=True # - Unable to get shapes??

empty_group = cmds.group(empty=True, name=selection)
selected_shapes = []


for shape in selection_children:
    if "Shape" in shape:
        selected_shapes.append(shape)
 
 
# combine curves       
cmds.select(empty_group)
cmds.select(selected_shapes)  
        
cmds.parent(selected_shapes, empty_group, r=True, s=True)


# cleanup
cmds.delete(selection)
cmds.rename(empty_group, empty_group[:-1] + "_combined")