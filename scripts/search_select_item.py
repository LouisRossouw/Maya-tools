"""
Quick script to search and select a specific control / item etc

Author: www.LouisRossouw.com
"""

import maya.cmds as cmds


SEARCH_WORD = "legUI_L0_ctl" # add search word here.

sel = cmds.ls()
for i in sel:
    
    if i == SEARCH_WORD:
        cmds.select(i)