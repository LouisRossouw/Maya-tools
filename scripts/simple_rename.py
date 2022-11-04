import maya.cmds as cmds

selected = cmds.ls(selection=True)

new_name = "chips_geo_"

count = 0
for child in selected:
    count += 1
    
    cmds.rename(child, new_name + str(count))
