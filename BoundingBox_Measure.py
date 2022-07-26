"""
Simply returns the measurements of an object based on its bounding box size.

Author: www.LouisRossouw.com
"""

import maya.cmds as cmds


sel = cmds.ls(selection=True)
Unit_measurement = cmds.currentUnit(query=True, linear=True)

# X min | Y min | Z min ||| X max | Y max | Z max
BBOX = cmds.exactWorldBoundingBox(sel[0])

Xmin = BBOX[0]
Ymin = BBOX[1]
Zmin = BBOX[2]

Xmax = BBOX[3]
Ymax = BBOX[4]
Zmax = BBOX[5]

Xwidth_scale = Xmax - Xmin
Yheight_scale = Ymax - Ymin
Zdepth_scale = Zmax - Zmin

Output = f"X - {round(Xwidth_scale, 2)} {Unit_measurement}\nY - {round(Yheight_scale, 2)} {Unit_measurement}\nZ - {round(Zdepth_scale, 2)} {Unit_measurement}"

cmds.confirmDialog(title="BoundingBox Measurements", message=sel[0] + "\n\n" + Output)