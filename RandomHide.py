"""
Randomly animates objects disapearing in a randomised way, good for pixle art fade out

Author: www.LouisRossouw.com
"""

import random
import maya.cmds as cmds



frame_START = 100
frame_END = 125

sel = cmds.ls(selection=True)
selection_children = cmds.listRelatives(sel, ad=True)

obj_list = []
frame_range = []

# Collects all children nodes without Shape, and appends them to a list
for obj in selection_children:
	if "Shape" not in obj:
		obj_list.append(obj)
		
		
for frame in range(frame_START, frame_END + 1):
	frame_range.append(frame)
	
random.shuffle(frame_range)
random.shuffle(obj_list)

# Keys frame at random.
for obj in obj_list:
	
	frame = random.choice(frame_range)
	
	cmds.setKeyframe(obj + ".visibility" ,time=frame, v=1)
	cmds.setKeyframe(obj + ".visibility" ,time=frame + 1, v=0)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	




