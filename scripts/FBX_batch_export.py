
""" Export FBX. """

import pymel.core as pm

pm.loadPlugin("fbxmaya")

path = "D:/path/to/dir/"
sel = pm.ls(selection=True)

for obj in sel:
    pm.mel.FBXExport(f=path + obj)
