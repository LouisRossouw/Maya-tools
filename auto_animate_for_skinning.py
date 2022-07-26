"""
Quick dirty script to autoanimate controls to aid in skinning
"""

import maya.cmds as cmds
from functools import partial



def UI():
	def set_key(selected, axis_key, value, count):
		""" Simply sets key to given control and values """
		#print("keying", count, test)
		
		attr = ["tx", "ty", "tz", "rx", "ry", "rz"]
		
						
		# zero
		cmds.setKeyframe(
						selected,
						attribute=attr,
						time=[str(count)+'sec'],
						v=0
						)
		# zero
		cmds.setKeyframe(
						selected,
						attribute=axis_key,
						time=[str(count)+'sec'],
						v=value
						)
					
					
			
					
	def key(key_data, cntrls_list, selection_controls):
		""" applies key to specific """
		
		# loop through filtered data
		for cntrl in key_data:
			name = cntrl.split("_")[0]
			num = cntrl.split("_")[1]
					
			
			# loop through all the rigs controls
			count = 0
			for selected in selection_controls:
				
				# if name matches, set keys to the given values
				if cntrl in selected:
					if "ctl" in selected:
						if "Shape" not in selected:
							
							
							key_count = len(key_data[cntrl]) * 2
							for i in range(key_count):
								num_check = str(i/2).split(".")[1]
								cmds.setKeyframe(
												selected,
												at=["tx", "ty", "tz", "rx", "ry", "rz"],
												time=[str(i/2)+'sec'],
												v=0
												)
						
							for axis_key in key_data[cntrl]:
								
								count += 1
								value = key_data[cntrl][axis_key]
								
								set_key(selected, axis_key, value, count)
								
							# Shift keys back
							cmds.keyframe(selected, edit=True, relative=True, timeChange=-15)
		
		
		
		
		
	def return_controls(selection_children):
		""" returns a list of all the controls(children) within the selected rig """
		
		select_list = []
		
		for child in selection_children:
			select_list.append(child)
			
		return(select_list)
	
	
	
	
	
	def add_keys(cntrls_list, selection_controls, limb):
		""" algo to adds keys to specific body parts """
				
		for control_type in cntrls_list:
			
			data = {}
			
			# head
			if control_type == "neck_low":
				pass
			if control_type == "neck_mid":
				pass		
			if control_type == "head":
				pass
			
			# arm limbs
			if control_type == "shoulder":
				pass
				
			if control_type == "arm":
				data["arm_"+limb+"_fk0"] = {"ry":75, "rz":-90, "rotateY":-90, "rx":90, "rx":-90}
				key(data, cntrls_list, selection_controls)
				
			if control_type == "forarm":
				data["arm_"+limb+"_fk1"] = {"rz":-90}
				key(data, cntrls_list, selection_controls)	
				
			if control_type == "hand":
				pass		
							
			# spine
			if control_type == "spine_FK":
				pass
			if control_type == "spine_IK_chest":
				pass		
			if control_type == "spine_IK_pelvis":
				pass		
			# leg limbs
			if control_type == "leg":
				data["leg_LO_ik"] = {"ty":35, "tz":40}
				key(data, cntrls_list, selection_controls)	
				
			if control_type == "knee":
				pass		
			if control_type == "ankle":
				pass		
	
	
	
	
	def run(*args):
		
		left_checkbox_eval = cmds.checkBox(check_left, query=True, value=True)
		right_checkbox_eval = cmds.checkBox(check_right, query=True, value=True)
				
		print(args)
				
		control_search_list = ["arm"]
		
		selection = cmds.ls(selection=True)
		selection_children = cmds.listRelatives(selection, ad=True)
		selection_controls = return_controls(selection_children)
		
		#if left_checkbox_eval == True:
			#add_keys(control_search_list, selection_controls, limb="L0")
		#if right_checkbox_eval == True:
			#add_keys(control_search_list, selection_controls, limb="R0")
			
			
			
			
			
	# UI
	if cmds.window('QuickDirty_Key', exists=True):
		cmds.deleteUI('QuickDirty_Key')
	
	window = cmds.window(title='QuickDirty_Key', widthHeight=(350, 380) )
	
	cmds.columnLayout(adjustableColumn=True)
	cmds.frameLayout(label='dev', borderStyle='etchedOut', cll=True, mh=10, )
	cmds.rowColumnLayout(numberOfColumns=2, columnAttach=(1, 'right', 0), columnWidth=[(10, 100), (2, 250)])
	
	
	check_left = cmds.checkBox("Left", value=True)
	check_right = cmds.checkBox("Right")
	
	cmds.text(label="")
	arm_button = cmds.button(label="Shoulder", command=run)
	
	cmds.text(label="")
	arm_button = cmds.button(label="Arm", command=run)
	
	cmds.text(label="")
	arm_button = cmds.button(label="Forarm", command=run)
	
	cmds.text(label="")
	arm_button = cmds.button(label="Hand", command=run)

#	
	cmds.text(label="")
	cmds.separator(height=10)	
			
#		
	cmds.text(label="")
	arm_button = cmds.button(label="Leg", command=run)
	
	cmds.text(label="")
	arm_button = cmds.button(label="Knee", command=run)
	
	cmds.text(label="")
	arm_button = cmds.button(label="Ankle", command=run)
	

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	cmds.showWindow(window)
	
	
	
if __name__ == "__main__":
	
	UI()