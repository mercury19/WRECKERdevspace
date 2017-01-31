import sys
sys.dont_write_bytecode = True

import re


## set the files to WRECK. It is adivsed that you do NOT use this file to WRECK the following: module_constants, module_strings, module_info, and module_info_pages.
files_to_process = ['module_scripts', 'module_presentations', 'module_troops', 'module_items', 'module_game_menus'] 

identifier = {'spr_': 'spr.', 'icon_': 'icon.', 'prsnt_': 'prsnt.', 'p_': 'p.', 'psys_': 'psys.', 'mesh_': 'mesh.', 'itm_': 'itm.', 'qst_': 'qst.', 'tableau_': 'tableau.', 'pt_': 'pt.', 'trp_': 'trp.', 'ip_': 'ip.', 'mt_': 'mt.', 'anim_': 'anim.', 'pfx_': 'pfx.', 'snd_': 'snd.', 'scn_': 'scn.', 'mnu_': 'mnu.', 'imod_': 'imod.', 'skl_': 'skl.', 'script_': 'script.', 'track_': 'track.', 'fac_': 'fac.'}
old_id = identifier.keys()
new_id = identifier.values()

info = "\n\n###################################\n#   W.R.E.C.K. Compiler Options   #\n###################################\n\n\n# Change this line to select where compiler will generate ID_* files. Use None instead of the string to completely suppress generation of ID_* files.\n# ONLY DO THIS WHEN YOU HAVE COMPLETELY REMOVED ID_* FILE DEPENDENCIES IN MODULE SYSTEM!\n# Default value: \"ID_%s.py\"\n\n\n#write_id_files = \"ID_%s.py\"\n# default vanilla-compatible option\n#write_id_files = \"ID/ID_%s.py\"\n# will put ID_* files in ID/ subfolder of module system's folder\nwrite_id_files = None\n# will suppress generation of ID_*.py files\n\n\n# Set to True to display compiler performance information at the end of compilation. Set to False to suppress.\n# Default value: False\n\n\nshow_performance_data = True\n\n\n\n\n##########################\n#   W.R.E.C.K. Plugins   #\n##########################\n\n\n#import plugin_ms_extension\n#import plugin_presentations"


quote = '"'
score = "_"

final = "from compiler import *\n"

def find_char(string, char): 
  character = string[:1]
  if character is char:
    return -1
  else:
    pass

def find_old_ref(string):
  for r in range(0, len(identifier)):
    find_id = re.compile(r'[\s|\S]' + re.escape(old_id[r]) )
    non_ref = re.compile(r'\w' + re.escape(old_id[r]) )
    found = find_id.findall(string)
    references = [f for f in found if not non_ref.match(f)]
    for ref in references:
      isquote = find_char(ref, quote)
      if isquote == -1:
        quoted = string.find(quote+old_id[r])
        next_quote = string.find(quote, quoted+1)
        quoted_reference = string[quoted:next_quote+1]
        new_ref = quoted_reference.strip(quote).replace(old_id[r], new_id[r])
        new = string.replace(quoted_reference, new_ref)
        string = new
      else:
        new = re.sub(old_id[r], new_id[r], ref)
        final = string.replace(ref, new)
        string = final
  return string


def fix_string_refs(string):
  first = special_str.sub('s.1_', string)
  string = first
  find_str = re.compile(r'[\s|\S]' + 'str_')
  non_ref = re.compile(r'\w' + 'str_')
  found = find_str.findall(string)
  references = [f for f in found if not non_ref.match(f)]
  for ref in references:
    isquote = find_char(ref, quote)
    thing = string.find(ref)
    skip = not_str.findall(string)
    if isquote == -1:
      quoted = string.find('"str_')
      next_quote = string.find(quote, quoted+1)
      quoted_reference = string[quoted:next_quote+1]
      new_ref = quoted_reference.strip(quote).replace('str_', 's.')
      new = string.replace(quoted_reference, new_ref)
      string = new
    elif not_str.match(string[thing+1:]):
      pass
    else:
      new = re.sub('str_', 's.', ref)
      final = string.replace(ref, new, 1)
      string = final
  return string


def wrecker(filename):

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

def add_wrecker_options(filename):

  test = "W.R.E.C.K. Compiler Options"

  file = open(filename,"r")
  lines = file.readlines()
  file.close()

  if test in lines:
    print "expanding " + filename
    with open(filename, "a") as file:
      file.write(info)



def print_menu():
    print "#####################################################"
    print "A note on syntax:"
    print "a) For files in the same directory, do not add any extra prefixes or the '.py'"
    print "    Example: module_troops"
    print "   Just like that."
    print " "
    print "b) for files in subdirectories, add the subdirectory with a '/' after to the beginning of the file name"
    print "    Example: if I had all move module files in a subdirectory MDL, I would put MDL/module_troops"
    print " "
    print "This applies for files defined inside wrecker.py, as well as for any that you input through this menu."
    print "#####################################################"
    print "1) WRECK files"
    print "2) Input a file to WRECK"
    print "3) Add WRECk options to module_info.py - unnecessary if (1) has already been chosen."
    print "4) Print list of files to be WRECKED"
    print "0) Exit"  

def process():

  legal_choices = set(["0","1","2","3","4","9"])
  choice =""
  print_menu()
  while choice != "0":
    choice =""
    while not choice in legal_choices:
            choice = raw_input("Make a choice (4 to display menu again) >").lower()

            if choice == '1':
              all_files = len(files_to_process)
              print "processing..."
              for n in range(0, all_files):
                wrecker(files_to_process[n] + ".py")
                fix_imports(files_to_process[n] + ".py")
              expand_module_info("module_info.py")

            elif choice == '2':
              response = raw_input('Input a file to process: ')
              wrecker(response + ".py")
              fix_imports(response + ".py")

            elif choice == '3':
              expand_module_info("module_info.py")

            elif choice == '4':
              print "######## Files to be processed ########"
              print ""
              all_files = len(files_to_process)
              for n in range(0, all_files):
                print files_to_process[n]
                print ""


            elif choice == '5':
              print_menu()

if __name__ == '__main__':
  process()

