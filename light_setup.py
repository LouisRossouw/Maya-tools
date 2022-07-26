"""
Quickly adds a 3 point areaLight setup, with pivot points at origin, to help adjust angles.

Author: www.LouisRossouw.com
"""


import maya.cmds as cmds


LIGHT_COUNT = 3

LIGHT_TRAN_X = 1000
LIGHT_TRAN_Y = 100
LIGHT_ROT_X = -35
LIGHT_SCALES = 200
LIGHT_GROUP_Y = 100
INTENSITY = 60000

RX_LIGHT_LIST = [0, 125, -125]


lights = {}

for i in range(LIGHT_COUNT):

# Create 3 point Lights
    light_name = cmds.shadingNode('areaLight', asLight=True)
    
    cmds.setAttr(light_name[:-1]+"Shape"+str(i+1)+".intensity", INTENSITY)
    cmds.setAttr(light_name + ".tz",    LIGHT_TRAN_X)
    cmds.setAttr(light_name + ".scale", LIGHT_SCALES, 
                                        LIGHT_SCALES, 
                                        LIGHT_SCALES)

# group lights and center pivots
    light_group = cmds.group(name="light_grp_" + str(i))
    cmds.xform(light_group, piv=[0, 0, 0])
    lights[light_group] = light_name
    

# rotate individual sub light groups
count = -1
for light in lights:
    count += 1
    value = RX_LIGHT_LIST[count]
    cmds.setAttr(light + ".rx", LIGHT_ROT_X)
    cmds.setAttr(light + ".ry", value)
    
    
tmp_light_list = []
for light in lights:
    tmp_light_list.append(light)
    

# group and center pivot to the main light group
MAIN_LIGHT_GROUP = cmds.group(tmp_light_list, name="Lights")
cmds.xform(MAIN_LIGHT_GROUP, piv=[0, 0, 0])