"""
Produces a row of balls, its in a WIP 

Auther: www.LouisRossouw.com
"""

import maya.cmds as cmds



cmds.group(em=True, name="balls")
count = 0

translate = 0
ball_scale = 10

for i in range(3):

	count += 1	
	translate += 100

	ball_name = "Ball_"+str(count)
	ball = cmds.sphere(name=ball_name)
	cmds.setAttr(ball_name+".translateX", translate)
	
	cmds.setAttr(ball_name+".scaleX", ball_scale)
	cmds.setAttr(ball_name+".scaleY", ball_scale)
	cmds.setAttr(ball_name+".scaleZ", ball_scale)
		
	cmds.group(ball, parent="balls")
	
