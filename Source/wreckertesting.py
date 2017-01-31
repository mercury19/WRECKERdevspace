import sys
sys.dont_write_bytecode = True

import re



	# WRECK.anim[7] = animations
	# WRECK.fac[7] = factions
	# WRECK.ip[7] = info_pages
	# WRECK.imod[7] = item_modifiers
	# WRECK.itm[7] = items
	# WRECK.icon[7] = map_icons
	# WRECK.mnu[7] = game_menus
	# WRECK.mesh[7] = meshes
	# WRECK.mt[7] = mission_templates
	# WRECK.track[7] = tracks
	# WRECK.psys[7] = particle_systems
	# WRECK.p[7] = parties
	# WRECK.pt[7] = party_templates
	# WRECK.pfx[7] = postfx_params
	# WRECK.prsnt[7] = presentations
	# WRECK.qst[7] = quests
	# WRECK.spr[7] = scene_props
	# WRECK.scn[7] = scenes
	# WRECK.script[7] = scripts
	# WRECK.skl[7] = skills
	# WRECK.snd[7] = sounds
	# WRECK.s[7] = strings
	# WRECK.tableau[7] = tableaus
	# WRECK.trp[7] = troops

# str_clear, str_is_empty, str_store, str_encode, str_[0-9]

quote = '"'
score = "_"

identifier = {'spr_': 'spr.', 'icon_': 'icon.', 'prsnt_': 'prsnt.', 'p_': 'p.', 'psys_': 'psys.', 'mesh_': 'mesh.', 'itm_': 'itm.', 'qst_': 'qst.', 'tableau_': 'tableau.', 'pt_': 'pt.', 'trp_': 'trp.', 'ip_': 'ip.', 'mt_': 'mt.', 'anim_': 'anim.', 'pfx_': 'pfx.', 'snd_': 'snd.', 'scn_': 'scn.', 'mnu_': 'mnu.', 'imod_': 'imod.', 'skl_': 'skl.', 'script_': 'script.', 'track_': 'track.', 'fac_': 'fac.'}
old_id = identifier.keys()
new_id = identifier.values()

info = "\n\n###################################\n#   W.R.E.C.K. Compiler Options   #\n###################################\n\n\n# Change this line to select where compiler will generate ID_* files. Use None instead of the string to completely suppress generation of ID_* files.\n# ONLY DO THIS WHEN YOU HAVE COMPLETELY REMOVED ID_* FILE DEPENDENCIES IN MODULE SYSTEM!\n# Default value: \"ID_%s.py\"\n\n\n#write_id_files = \"ID_%s.py\"\n# default vanilla-compatible option\n#write_id_files = \"ID/ID_%s.py\"\n# will put ID_* files in ID/ subfolder of module system's folder\nwrite_id_files = None\n# will suppress generation of ID_*.py files\n\n\n# Set to True to display compiler performance information at the end of compilation. Set to False to suppress.\n# Default value: False\n\n\nshow_performance_data = True\n\n\n\n\n##########################\n#   W.R.E.C.K. Plugins   #\n##########################\n\n\n#import plugin_ms_extension\n#import plugin_presentations"


final = "from compiler import *\n"

special_str = re.compile(r'str_1_')
not_str = re.compile(r'(str_clear|str_is_empty|str_store|str_encode|str_\d)')








test_string = '(faction_set_note_available, "fac_no_faction", 0, itm_bolts, itm_str_axe), script_get_str_for_troop, (str_is_empty, "str_kingdom_6", str_kingdom_6, str_store_, str_1_denar, str_1_div), str_20'
test_string2 = '["wut_dafac_man","Maceman","Maceman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners, [itm_tutorial_club,itm_leather_jerkin,itm_hide_boots], str_6|agi_6|level(1),wp(50),knows_common,mercenary_face_1,mercenary_face_2],'
test_string3 = '(call_script, "script_give_center_to_faction_aux", "p_town_1", fac_kingdom_4, itm_bolts, create_mesh_overlay, "wut_dafac_man", "fac_kingdom_4"),'

# print not_str.findall(test_string)

def find_char(string, char): ##Function to to check the first character of a string.
  character = string[:1]
  if character is char:
    return -1
  else:
    pass


def fix_string_refs(string):
	first = special_str.sub('s.1_', string)
	string = first
	find_str = re.compile(r'[\s|\S]' + 'str_')
	non_ref = re.compile(r'\w' + 'str_')

	found = find_str.findall(string)

	references = [f for f in found if not non_ref.match(f)]
	# print references

	# print string

	

	for ref in references:
		# print ref
		isquote = find_char(ref, quote)
		thing = string.find(ref)
		# print thing
		skip = not_str.findall(string)
		# print skip
		if isquote == -1:
			quoted = string.find('"str_')
			next_quote = string.find(quote, quoted+1)
			quoted_reference = string[quoted:next_quote+1]
			new_ref = quoted_reference.strip(quote).replace('str_', 's.')
			new = string.replace(quoted_reference, new_ref)
			string = new
			# print string
		elif not_str.match(string[thing+1:]):
			pass
		else:
			new = re.sub('str_', 's.', ref)
			final = string.replace(ref, new, 1)
			string = final
			# print string

	# print string

	return string
		



# fix_string_refs(test_string)













def find_old_ref(string):
	for r in range(0, len(identifier)):
		find_id = re.compile(r'[\s|\S]' + re.escape(old_id[r]) )
		non_ref = re.compile(r'\w' + re.escape(old_id[r]) )
		found = find_id.findall(string)
		# print found
		references = [f for f in found if not non_ref.match(f)]
		# print references
		for ref in references:
			# print ref
			isquote = find_char(ref, quote)
			# print isquote
			if isquote == -1:
				quoted = string.find(quote+old_id[r])
				print quoted
				next_quote = string.find(quote, quoted+1)
				quoted_reference = string[quoted:next_quote+1]
				# print quoted
				# print '"'+old_id[r]
				# print next_quote
				# print quoted_reference
				new_ref = quoted_reference.strip(quote).replace(old_id[r], new_id[r])
				# print new_ref
				new = string.replace(quoted_reference, new_ref)
				# print new
				string = new
			else:
				new = re.sub(old_id[r], new_id[r], ref)
				final = string.replace(ref, new)
				# print final
				# print new_id[r]
				# print new
				string = final


	print string

	return string

find_old_ref(test_string3)


def fix_imports(filename):

	print "Fixing imports in " + filename
	file = open(filename,"r")
	lines = file.readlines()
	file.close()

	file = open(filename,"w")

	imports = []
	for line in lines:
		if line is lines[0]:
			lines[0] = final
			line = lines[0]
		is_import = find_char(line, "f")
		if is_import:
			imports.append(line)
		discard = imports[1:]
		if line not in discard:
			file.write("%s"%line)
	file.close()


# fix_imports("bogus_import_file.py")
# fix_imports("module_presentations.py")








def process(filename):

	print "Fixing references in " + filename
	file = open(filename,"r")
	lines = file.readlines()
	file.close()

	file = open(filename,"w")

	for line in lines:
		start = find_old_ref(line)
		line = start
		finish = fix_string_refs(line)
		line = finish
		file.write("%s"%line)
	file.close()

# process("bogus_import_file.py")

def add_wrecker_options(filename):

	test = "W.R.E.C.K. Compiler Options"

	file = open(filename,"r")
	lines = file.readlines()
	file.close()

	if test in lines:
		print "expanding " + filename
		with open(filename, "a") as file:
			file.write(info)



# expand_module_info("bogus_import_file.py")


# print info

# process("bogus_import_file.py")
# fix_imports("bogus_import_file.py")
# expand_module_info("bogus_import_file.py")
