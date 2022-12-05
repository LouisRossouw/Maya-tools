""" Freeze transform on children. """

import maya.cmds as cmds

selection = cmds.ls(selection=True)
selection_children = cmds.listRelatives(selection, ad=True)

for child in selection_children:
    
    if "Shape" not in child:
        
        print(child)
        
        cmds.select(child)
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        
        
