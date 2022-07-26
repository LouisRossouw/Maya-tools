""" 
Script to globally shift ALL scene keys by frame amount.

Author: www.LouisRossouw.com
"""
import maya.cmds as cmds


SHIFTAMOUNT = 100 # Frames amount

cmds.select(cmds.ls(type='animCurve'))
cmds.selectKey()
cmds.keyframe(animation="keys", edit=True,relative=True,timeChange=SHIFTAMOUNT)


