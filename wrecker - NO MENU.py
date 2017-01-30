import sys
sys.dont_write_bytecode = True

import re


identifier = { 0 : "anim", 1 : "fac", 2 : "ip", 3 : "imod", 4 : "itm", 5 : "icon", 6 : "mnu", 7 : "mesh", 8 : "mt", 9 : "track", 10 : "psys", 11 : "p", 12 : "pt", 13 : "pfx", 14 : "prsnt", 15 : "qst", 16 : "spr", 17 : "scn", 18 : "script", 19 : "skl", 20 : "snd", 21 : "tableau", 22 : "trp" }



## set the files to WRECK. It is adivsed that you do NOT use this file to WRECK the following: module_constants, module_strings, module_info, and module_info_pages.
files_to_process = ['module_scripts', 'module_presentations', 'module_troops', 'module_items', 'module_game_menus'] 






quote = '"'
score = "_"

all_identifiers = len(identifier) 
length = range(0, all_identifiers)
update = [identifier[i]+"." for i in range(0, all_identifiers)]
old_id = [identifier[i]+score for i in range(0, all_identifiers)]
new_id = dict(zip(length, update))

final = "from compiler import *\n"

def find_char(string, char): 
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
    references = [f for f in found if not non_ref.match(f)]
    for ref in references:
      isquote = find_char(ref, quote)e
      if isquote == -1:
        quoted = string.find(old_id[r])
        next_quote = string.find(quote, quoted)
        quoted_reference = string[quoted-1:next_quote+1]e
        new_ref = quoted_reference.strip(quote).replace(old_id[r], new_id[r])
        new = string.replace(quoted_reference, new_ref)
        string = new
      else:
        new = re.sub(old_id[r], new_id[r], ref)
        final = string.replace(ref, new)
        string = final
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

