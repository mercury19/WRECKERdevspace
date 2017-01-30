import sys
sys.dont_write_bytecode = True

import re


quote = '"'
score = "_"

identifier = ["itm", "fac", "mesh"] ## set your reference identifiers
all_identifiers = len(identifier) 
old_id = [identifier[i]+score for i in range(0, all_identifiers)]
new_id = [identifier[i]+"." for i in range(0, all_identifiers)]

final = "from compiler import *\n"

# print all_identifiers ## 2
# print range(0, all_identifiers) ## [0, 1]
# print identifier[0] ## itm
# print old_id ## ['itm_', 'fac_']
# print new_id ## ['itm.', 'fac.']
# print new_id[0] ## itm.

test_string = '(faction_set_note_available, "fac_no_faction", 0, itm_bolts),'
test_string2 = '["tutorial_maceman","Maceman","Maceman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners, [itm_tutorial_club,itm_leather_jerkin,itm_hide_boots], str_6|agi_6|level(1),wp(50),knows_common,mercenary_face_1,mercenary_face_2],'
test_string3 = '(call_script, "script_give_center_to_faction_aux", "p_town_1", "fac_kingdom_4", itm_bolts, create_mesh_overlay),'

def find_char(string, char): ##Function to to check the first character of a string.
  character = string[:1]
  if character is char:
    return -1
  else:
    pass


def find_old_ref(string):
	for r in range(0, len(old_id)):
		static = string.find(old_id[r])
		quoted = string.find(quote+old_id[r])
		non_ref = string.find(score+old_id[r])
		# print non_ref
		# print ""
		# print quoted 
		# print ""
		# print static
		# print ""
		# print ""
		if static != -1 and quoted != -1 and non_ref == -1:
			next_quote = string.find(quote, static)
			quoted_reference = string[quoted:next_quote+1]
			# print quoted
			# print '"'+old_id[r]
			# print next_quote
			# print quoted_reference
			new_ref = quoted_reference.strip(quote)
			# print new_ref
			new = string.replace(quoted_reference, new_ref).replace(old_id[r], new_id[r])
			# print new
			string = new
		elif quoted == -1 and static != -1 and non_ref == -1:
			# print static
			# print old_id[r]
			new = string.replace(old_id[r], new_id[r])
			# print new_id[r]
			# print new
			string = new
		elif non_ref != -1:
			pass

	return string

# find_old_ref(test_string3)


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
fix_imports("module_presentations.py")








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

# process("module_presentations.py")









# find_id = [r for r in old_id if id in r]
# find_new = [n for n in new_id if id in n]



