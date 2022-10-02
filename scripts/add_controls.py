""" Creates controls around an objects center point. its still an wip. """


import maya.cmds as cmds



def query_size(Xdistance, Zdistance):

    into_list = [Xdistance, Zdistance]
    get_min = min(into_list)
    get_max = max(into_list)

    if get_max > (get_min * 2):
        query = True
    else:
        query = False

    return(query)



def get_average(num1, num2):
  return (int(num1) + int(num2)) / 2.0




def combine_shapes(selection, name):

    # selection = cmds.ls(selection=True)[0]
    selection_children = cmds.listRelatives(selection, ad=True)  # shape=True # - Unable to get shapes??

    empty_group = cmds.group(empty=True, name=name)
    selected_shapes = []

    for shape in selection_children:
        if "Shape" in shape:
            selected_shapes.append(shape)

    # combine curves
    cmds.select(empty_group)
    cmds.select(selected_shapes)

    cmds.parent(selected_shapes, empty_group, r=True, s=True)

    # cleanup
    cmds.delete(selection)
    cmds.rename(empty_group, empty_group[:-1])



def create_controls(type, name):

    if type.lower() == "square":
        control = cmds.nurbsSquare(name=name)
        combine_shapes(control, name)
    elif type.lower() == "circle":
        control = cmds.circle(name=name)

    return(name)



def main():


    CONTROLS = ["master", "tran" ,"rot"]
    CONTROL_TYPE = "circle"



    sel = cmds.ls(selection=True)

    for i in sel:

        controls_dict_data = {}
        controls_list_data = []


        count = 0

        for control in CONTROLS:

            # X min | Y min | Z min ||| X max | Y max | Z max
            WRLD_boundBox = cmds.exactWorldBoundingBox(i)

            Xmin = WRLD_boundBox[0]
            Ymin = WRLD_boundBox[1]
            Zmin = WRLD_boundBox[2]

            Xmax = WRLD_boundBox[3]
            Ymax = WRLD_boundBox[4]
            Zmax = WRLD_boundBox[5]

            Xdistance = Xmax - Xmin
            Ydistance = Ymax - Ymin
            Zdistance = Zmax - Zmin

            query_eval = query_size(Xdistance, Zdistance)
            avarage_number = get_average(Xdistance, Zdistance)


            # re-scale the children controls in proportion to the master.
            count += 1
            if count != 1:
                scale_xyz = avarage_number - (avarage_number / 7)
            else:
                scale_xyz = avarage_number


            # cmds.select(i)
            master_name = i + "_" + control + "_ctl"
            master_control = create_controls(CONTROL_TYPE, master_name)


            cmds.matchTransform(master_control, i, pos=True)
            cmds.setAttr(master_name + ".rotateX", 90)

            # scale control
            cmds.setAttr(master_name + ".scale", scale_xyz, scale_xyz, Ydistance)

            controls_dict_data[master_control] = {"WRLD_boundBox" : WRLD_boundBox, "avarage_number" : scale_xyz}








if __name__ == "__main__":
    main()
