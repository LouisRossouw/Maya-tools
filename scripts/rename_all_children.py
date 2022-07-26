"""
Lists all children and renames them.

Author: www.LouisRossouw.com
"""



import maya.cmds as cmds


NEW_NAME = "machine_geo_" # add new name here.

selection = cmds.ls(selection=True)
selection_children = cmds.listRelatives(selection, ad=True)

count = 0
for child in selection_children:
	count += 1
	print(child)
	cmds.rename(child, NEW_NAME+ str(count))
                
            
