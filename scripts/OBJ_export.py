"""
Exports objs.

Author: www.LouisRossouw.com
"""

import maya.cmds as cmds


path = "" # add path here.
selected = cmds.ls(selection=True , sn=False)
	
for obj in selected:

    cmds.select(obj)
    cmds.file(path + "\\" + obj[1:]+".obj" , force=True, type="OBJexport", exportSelected=True)