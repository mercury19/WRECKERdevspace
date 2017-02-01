import sys
sys.dont_write_bytecode = True

from os.path import split as path_split, exists as path_exists
import re


## unused: ['animations', 'quests', 'strings', ] no references to outside files
file_names = ['constants', 'dialogs', 'factions', 'game_menus', 'items', 'map_icons', 'meshes', 'mission_templates', 'music', 'particle_systems', 'parties', 'party_templates', 'postfx', 'presentations', 'scene_props', 'scenes', 'scripts', 'simple_triggers', 'skills', 'skins', 'sounds', 'tableau_materials', 'triggers', 'troops'] 
modules = ['module_' + n for n in file_names]
headers = ['header_' + n for n in file_names]
headers_sub = ['headers/' + h for h in headers]

headers_package = path_exists('./headers')

## unused: [, 'tableau_': 'tableau.' 'spr_': 'spr.', ] all quoted references
identifier = {'icon_': 'icon.', 'prsnt_': 'prsnt.', 'p_': 'p.', 'psys_': 'psys.', 'mesh_': 'mesh.', 'itm_': 'itm.', 'qst_': 'qst.', 'pt_': 'pt.', 'trp_': 'trp.', 'ip_': 'ip.', 'mt_': 'mt.', 'anim_': 'anim.', 'pfx_': 'pfx.', 'snd_': 'snd.', 'scn_': 'scn.', 'mnu_': 'mnu.', 'imod_': 'imod.', 'skl_': 'skl.', 'script_': 'script.', 'track_': 'track.', 'fac_': 'fac.'}
old_id = identifier.keys()
new_id = identifier.values()

info = "\n\n###################################\n#   W.R.E.C.K. Compiler Options   #\n###################################\n\n\n# Change this line to select where compiler will generate ID_* files. Use None instead of the string to completely suppress generation of ID_* files.\n# ONLY DO THIS WHEN YOU HAVE COMPLETELY REMOVED ID_* FILE DEPENDENCIES IN MODULE SYSTEM!\n# Default value: \"ID_%s.py\"\n\n\n#write_id_files = \"ID_%s.py\"\n# default vanilla-compatible option\n#write_id_files = \"ID/ID_%s.py\"\n# will put ID_* files in ID/ subfolder of module system's folder\nwrite_id_files = None\n# will suppress generation of ID_*.py files\n\n\n# Set to True to display compiler performance information at the end of compilation. Set to False to suppress.\n# Default value: False\n\n\nshow_performance_data = True\n\n\n\n\n##########################\n#   W.R.E.C.K. Plugins   #\n##########################\n\n\n#import plugin_ms_extension\n#import plugin_presentations"


quote = '"'
score = "_"

final = "from compiler import *\n"

special_str = re.compile(r'str_1_')
not_str = re.compile(r'(str_clear|str_is_empty|str_store|str_encode|str_\d)')

def find_char(string, char): 
  character = string[:1]
  if character is char:
    return -1
  else:
    pass

def find_old_ref(string):
  for r in range(0, len(identifier)):
    find_id = re.compile(r'[\s|\S]' + re.escape(old_id[r]) )
    non_ref = re.compile(r'[\w."]' + re.escape(old_id[r]) )
    found = find_id.findall(string)
    references = [f for f in found if not non_ref.match(f)]
    for ref in references:
      # isquote = find_char(ref, quote) ## Quoteed reference replacement deprecated. The number of errors it generated outweighed any desire for consistency, and it's unecessary anyway.
      # if isquote == -1:
      #   quoted = string.find(quote+old_id[r])
      #   next_quote = string.find(quote, quoted+1)
      #   quoted_reference = string[quoted:next_quote+1]
      #   new_ref = quoted_reference.strip(quote).replace(old_id[r], new_id[r], 1)
      #   new = string.replace(quoted_reference, new_ref)
      #   string = new
      # else:
      new = re.sub(old_id[r], new_id[r], ref, 1)
      final = string.replace(ref, new)
      string = final
  return string

## Deprecated; All string references to remain quoted, as they contain special characters(=, +, etc.) which mess with the compiler otherwise.
# def fix_string_refs(string):
#   first = special_str.sub('s.1_', string)
#   string = first
#   find_str = re.compile(r'[\s|\S]' + 'str_')
#   non_ref = re.compile(r'[\w.]' + 'str_' + r'[_]')
#   found = find_str.findall(string)
#   references = [f for f in found if not non_ref.match(f)]
#   for ref in references:
#     isquote = find_char(ref, quote)
#     thing = string.find(ref)
#     skip = not_str.findall(string)
#     if isquote == -1:
#       quoted = string.find('"str_')
#       next_quote = string.find(quote, quoted+1)
#       quoted_reference = string[quoted:next_quote+1]
#       new_ref = quoted_reference.strip(quote).replace('str_', 's.', 1)
#       new = string.replace(quoted_reference, new_ref)
#       string = new
#     elif not_str.match(string[thing+1:]):
#       pass
#     else:
#       new = re.sub('str_', 's.', ref)
#       final = string.replace(ref, new, 1)
#       string = final
#   return string


def wrecker(filename):
  print "Fixing references in " + filename
  file = open(filename,"r")
  lines = file.readlines()
  file.close()

  file = open(filename,"w")

  for line in lines:
    start = find_old_ref(line)
    line = start
    # finish = fix_string_refs(line)
    # line = finish
    file.write("%s"%line)
  file.close()


def fix_imports(filename):
  print "Fixing imports in " + filename
  file = open(filename,"r")
  lines = file.readlines()
  file.close()

  file = open(filename,"w")
  add_new = [final] + lines
  lines = add_new

  imports = []
  for line in lines:
    is_import = line.startswith("from")
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

  if test not in lines:
    print "expanding " + filename
    with open(filename, "a") as file:
      file.write(info)


for f in files_to_process:
  wrecker(modules[n] + ".py")
  fix_imports(modules[n] + ".py")
  try:
    if headers_package:
      fix_imports(headers_sub[n] + ".py")
      fix_imports("headers/header_common.py")
    else:
      fix_imports(headers[n] + ".py")
      fix_imports("header_common.py")
    except:
      pass 
  add_wrecker_options("module_info.py")


