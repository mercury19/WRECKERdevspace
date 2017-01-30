import sys
sys.dont_write_bytecode = True


## set your reference identifiers. At the moment, you cannot use this file for strings. The old prefix was "str_", while WRECK uses "s.". The functions defined below only work if the new and old identifiers are the same. Please plan accordingly.
identifier = ["itm", "fac", "mesh", "script", "prsnt", "mnu", "trp"] 


## set the files to WRECK. It is adivsed that you do NOT use this file to WRECK the following: module_constants, module_strings, module_info, and module_info_pages.
files_to_process = ['module_scripts', 'module_presentations', 'module_troops', 'module_items', 'module_game_menus'] 






quote = '"'
score = "_"

all_identifiers = len(identifier) 
old_id = [identifier[i]+score for i in range(0, all_identifiers)]
new_id = [identifier[i]+"." for i in range(0, all_identifiers)]

final = "from compiler import *\n"

def find_char(string, char): 
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
		if static != -1 and quoted != -1 and non_ref == -1:
			next_quote = string.find(quote, static)
			quoted_reference = string[quoted:next_quote+1]
			new_ref = quoted_reference.strip(quote)
			new = string.replace(quoted_reference, new_ref).replace(old_id[r], new_id[r])
			string = new
		elif quoted == -1 and static != -1 and non_ref == -1:
			new = string.replace(old_id[r], new_id[r])
			string = new
		elif non_ref != -1:
			pass
	return string


def wrecker(filename):

	print "Fixing references in " + filename
	file = open(filename,"r")
	lines = file.readlines()
	file.close()

	file = open(filename,"w")

	for line in lines:
		fixed = find_old_ref(line)
		if fixed != -1:
			line = fixed
		else:
			pass
		file.write("%s"%line)
	file.close()


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


for f in files_to_process:
  wrecker(f + ".py")
  fix_imports(f + ".py")

