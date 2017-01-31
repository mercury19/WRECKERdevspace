from compiler import *



####################################################################################################################
#  Each presentation record contains the following fields:
#  1) Presentation id: used for referencing presentations in other files. The prefix prsnt. is automatically added before each presentation id.
#  2) Presentation flags. See header_presentations.py for a list of available flags
#  3) Presentation background mesh: See module_meshes.py for a list of available background meshes
#  4) Triggers: Simple triggers that are associated with the presentation
####################################################################################################################

presentations = [
  ("game_credits",prsntf_read_only,mesh.load_window,[
      (ti_on_presentation_load,
       [(assign, "$g_presentation_credits_obj_1", -1),
        (assign, "$g_presentation_credits_obj_2", -1),
        (assign, "$g_presentation_credits_obj_3", -1),
        (assign, "$g_presentation_credits_obj_4", -1),
        (assign, "$g_presentation_credits_obj_5", -1),
        (assign, "$g_presentation_credits_obj_6", -1),
        (assign, "$g_presentation_credits_obj_7", -1),
        (assign, "$g_presentation_credits_obj_8", -1),
        (assign, "$g_presentation_credits_obj_9", -1),
        (assign, "$g_presentation_credits_obj_10", -1),
        (assign, "$g_presentation_credits_obj_11", -1),
        (assign, "$g_presentation_credits_obj_12", -1),
        (assign, "$g_presentation_credits_obj_1_alpha", 0),
        (assign, "$g_presentation_credits_obj_2_alpha", 0),
        (assign, "$g_presentation_credits_obj_3_alpha", 0),
        (assign, "$g_presentation_credits_obj_4_alpha", 0),
        (assign, "$g_presentation_credits_obj_5_alpha", 0),
        (assign, "$g_presentation_credits_obj_6_alpha", 0),
        (assign, "$g_presentation_credits_obj_7_alpha", 0),
        (assign, "$g_presentation_credits_obj_8_alpha", 0),
        (assign, "$g_presentation_credits_obj_9_alpha", 0),
        ]),



  ["arena_training_fighter_1","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.hide_boots],
   str_6|agi_6|level(5),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_2","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.hide_boots],
   str_7|agi_6|level(7),wp(70),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_3","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.hide_boots],
   str_8|agi_7|level(9),wp(80),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_4","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.hide_boots],
   str_8|agi_8|level(11),wp(90),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_5","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.hide_boots],
   str_9|agi_8|level(13),wp(100),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_6","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.hide_boots],
   str_10|agi_9|level(15),wp(110),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_7","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.hide_boots],
   str_10|agi_10|level(17),wp(120),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_8","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.hide_boots],
   str_11|agi_10|level(19),wp(130),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_9","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.hide_boots],
   str_12|agi_11|level(21),wp(140),knows_common,mercenary_face_1, mercenary_face_2],
  ["qut_dafac_man","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.hide_boots],
   str_12|agi_12|level(23),wp(150),knows_common,mercenary_face_1, mercenary_face_2],

  ["cattle","Cattle","Cattle",0,no_scene,reserved,fac.neutral, [], def_attrib|level(1),wp(60),0,mercenary_face_1, mercenary_face_2],


    (try_begin),
         (eq, ":item_situation", 0),
         (str_store_string, s0, s.open_gate, itm.bolts),
       (else_try), 
         (str_store_string, s0, s.close_gate),
       (try_end),

###################################
#   W.R.E.C.K. Compiler Options   #
###################################


# Change this line to select where compiler will generate ID_* files. Use None instead of the string to completely suppress generation of ID_* files.
# ONLY DO THIS WHEN YOU HAVE COMPLETELY REMOVED ID_* FILE DEPENDENCIES IN MODULE SYSTEM!
# Default value: "ID_%s.py"


#write_id_files = "ID_%s.py"
# default vanilla-compatible option
#write_id_files = "ID/ID_%s.py"
# will put ID_* files in ID/ subfolder of module system's folder
write_id_files = None
# will suppress generation of ID_*.py files


# Set to True to display compiler performance information at the end of compilation. Set to False to suppress.
# Default value: False


show_performance_data = True




##########################
#   W.R.E.C.K. Plugins   #
##########################


#import plugin_ms_extension
#import plugin_presentations