"""
Quick dirty script to select all fingers of any
rig with "finger" and ctl in the naming

Author: www.LouisRossouw.com
"""


import maya.cmds as cmds


selection = cmds.ls(selection=True)
selection_children = cmds.listRelatives(selection, ad=True)

new_select_list = []

for child in selection_children:

    if "finger" in child or "thumb" in child:
        if "ctl" in child:
            if "Shape" not in child:
        
                new_select_list.append(child)
                               
cmds.select(new_select_list)
            