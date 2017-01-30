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
    print "3) Print list of files to be WRECKED"
    print "0) Exit"  

def process():

  legal_choices = set(["0","1","2","3","4"])
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

            elif choice == '2':
              response = raw_input('Input a file to process: ')
              wrecker(response + ".py")
              fix_imports(response + ".py")

            elif choice == '3':
              print "######## Files to be processed ########"
              print ""
              all_files = len(files_to_process)
              for n in range(0, all_files):
                print files_to_process[n]
                print ""


            elif choice == '4':
              print_menu()

if __name__ == '__main__':
  process()

