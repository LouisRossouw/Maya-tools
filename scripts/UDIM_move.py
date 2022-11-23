""" Dirty script / UI to move UVs relatively to other tiles. """ 

import maya.cmds as cmds


def push_right(*args):
    cmds.polyEditUV(relative=True, uValue=1, vValue=0)


def push_left(*args):
    cmds.polyEditUV(relative=True, uValue=-1, vValue=0)


def push_up(*args):
    cmds.polyEditUV(relative=True, uValue=0, vValue=1)


def push_down(*args):
    cmds.polyEditUV(relative=True, uValue=0, vValue=-1)



def ui():
	""" Runs the UI """

	window_title = 'UDM Poosher'

	cmds.window(title=window_title, widthHeight=(400, 100), menuBar=True)

	cmds.columnLayout(adjustableColumn=True)
	cmds.rowColumnLayout(numberOfColumns=2, columnAttach=(1, 'right', 0), columnWidth=[(10, 100), (2, 250)])

	start_frame = cmds.playbackOptions(q=True, min=True)
	end_frame = cmds.playbackOptions(q=True, max=True)

	cmds.setParent( '..' )
	cmds.columnLayout(adjustableColumn=True)

	cmds.button(label='LEFT',bgc=(0.65, 1, 0), command=push_left)
	cmds.button(label='RIGHT',bgc=(0.65, 1, 0), command=push_right)
	
	cmds.button(label='UP',bgc=(0.65, 1, 0), command=push_up)
	cmds.button(label='DOWN',bgc=(0.65, 1, 0), command=push_down)
	
	cmds.setParent('..', menu=True)

	cmds.showWindow()

ui()


