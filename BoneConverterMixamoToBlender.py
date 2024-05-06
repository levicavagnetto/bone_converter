import bpy
import sys
import os

def main():
    # Get the active object (should be the armature)
    armature = bpy.context.active_object
    
    name_change_list = [("Mixamo Bone Name", "Blender Bone Name")]
    
    # Check if the active object is an armature
    if armature and armature.type == 'ARMATURE':
        # Access the bones in the armature
        bones = armature.data.bones
        
        # Iterate over each bone and rename it
        for bone in bones:
#            new_bone_name = bone.name;
#            if ".L" in bone.name:
#                new_bone_name = bone.name.replace(".L", "")
#            
#            if ".R" in bone.name and "Left" in bone.name:
#                new_bone_name = bone.name.replace("Left", "Right")
#                new_bone_name = new_bone_name.replace(".R", "")
            
#            if bone.name != new_bone_name:
#                print(bone.name + " -> " + new_bone_name)
#                bone.name = new_bone_name
#                for vg in armature.vertex_groups:
#                    if vg.name == bone.name:
#                        vg.name = new_name
            print(bone.name)
            
            new_name = bone.name
            
            new_name = new_name.replace("mixamorig:", "")
            
            if "Left" in new_name:
                new_name = new_name.replace("Left", "")
                new_name += ".L"
            if "Right" in new_name:
                new_name = new_name.replace("Right", "")
                new_name += ".R"
            
            name_change_list.append((bone.name, new_name))
            
    else:
        print("Active object is not an armature.")
        
    for item in name_change_list:
        print(item[0] + " -> " + item[1])
    

if __name__ == "__main__":
    main()
    print("==========================")