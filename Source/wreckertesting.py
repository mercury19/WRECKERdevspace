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



quote = '"'
score = "_"

identifier = { 0 : "anim", 1 : "fac", 2 : "ip", 3 : "imod", 4 : "itm", 5 : "icon", 6 : "mnu", 7 : "mesh", 8 : "mt", 9 : "track", 10 : "psys", 11 : "p", 12 : "pt", 13 : "pfx", 14 : "prsnt", 15 : "qst", 16 : "spr", 17 : "scn", 18 : "script", 19 : "skl", 20 : "snd", 21 : "tableau", 22 : "trp" }

all_identifiers = len(identifier) 

length = range(0, all_identifiers)

# rename = {"str" : "s"}
update = [identifier[i]+"." for i in range(0, all_identifiers)]

old_id = [identifier[i]+score for i in range(0, all_identifiers)]
# print old_id[2]

new_id = dict(zip(length, update))
# print update_id



# print update
# print rename
# print update_id



final = "from compiler import *\n"

# print all_identifiers ## 2
# print range(0, all_identifiers) ## [0, 1]
# print identifier[0] ## itm
# print old_id ## ['itm_', 'fac_']
# print new_id ## ['itm.', 'fac.']
# print new_id[0] ## itm.

test_string = '(faction_set_note_available, "fac_no_faction", 0, itm_bolts),'
test_string2 = '["wut_dafac_man","Maceman","Maceman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners, [itm_tutorial_club,itm_leather_jerkin,itm_hide_boots], str_6|agi_6|level(1),wp(50),knows_common,mercenary_face_1,mercenary_face_2],'
test_string3 = '(call_script, "script_give_center_to_faction_aux", "p_town_1", "fac_kingdom_4", itm_bolts, create_mesh_overlay, "wut_dafac_man", fac_kingdom_4),'

def find_char(string, char): ##Function to to check the first character of a string.
  character = string[:1]
  if character is char:
    return -1
  else:
    pass


def find_old_ref(string):
	for r in range(0, len(old_id)):
		change = 0

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
				quoted = string.find(old_id[r])
				# print quoted
				next_quote = string.find(quote, quoted)
				quoted_reference = string[quoted-1:next_quote+1]
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
		fixed = find_old_ref(line)
		line = fixed
		file.write("%s"%line)
	file.close()

process("bogus_import_file.py")









# # find_id = [r for r in old_id if id in r]
# # find_new = [n for n in new_id if id in n]



