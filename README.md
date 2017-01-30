# WRECKER-0.3b


It CAN:

	* Go through any specified files and change all specified native references to WRECK dynamic references.
	* This applies for both quoted and static references. Both "fac_kingdom_6" and fac_kingdom_6 become fac.kingdom_6, so you only have to keep track of one.
	* Ignore references in the middle of constants, script names, etc., "create_mesh_overlay" for example.
	* Access files in a subdirectory if you want to change some old files that have quoted references to dynamic ones, for example.
	* Replace all imports with a single "from compiler import *"
	* Ignore identifiers at the end of words, spt_ vs pt_ for example. pt_ is the party_templates identifier, which we want to change, while spt_ is a constant, which we don't want to change.

It CANNOT:

	* Change string references. At the moment there are far too many objects that use "str_" but are not strings for string references to be replaced by the current algorithm

In addition, I would avoid using this for module_strings, module_dialogs, module_constants, and module_info/pages. I haven't thoroughly examined those files so I don't know there are things that would be replaced, but shouldn't be.




INSTALLATION:
	
	1) Download one of the two "WRECKER" files. You don't need both, just choose one. 
		a) If you want to, download the matching .bat file. There's really no reason not too but it's technically optional. 

	2) Put the "WRECKER" file (and .bat if you have it) in the same folder as your "module_" files. Boom. Installed.


USE:

	1) Run the program. Its easiest to do this using the .bat, but if you don't want to use it you can also just run it with python. If you do it this way, make sure that all ".py" files are set to open with python as the default program. It won't work otherwise.
		a) To set files for the program to WRECK, open up "WRECKER" in a text editor and find "files_to_process". It should be near the top. Add your the files you want to run, without the file extensions. Follow the examples already there. Duplicate this process for reference prefixes, if desired. These are listed under "identifier", right above "files_to_process".

	2) If you downloaded the regular version, follow the on-screen menu. If not, watch it run. All done. 

Questions, comments, bugs, and source code:

	* All questions, comments, an dbug reports can be sent to mercury19 on the taleworlds forums, or posted in the WRECK thread, here: https://forums.taleworlds.com/index.php/topic,325102.0.html
	* If you want to work on WRECKER, go for it. You can request a pull from here, or just download the source folder and go to town. The source code is Native 1.171. I did not inlcude WRECK because I didn't find it necessary for creating WRECKER. I use wreckertesting.py for testing new ideas, and then copy the necessary code into wrecker.py, but you can do what you want. If you add stuff let me know so I can check it out, and possibly use your better version :P

Also, go ahead and ignore the sublime files~


CHANGELOG:

	0.3b:

		* Wrecker will now ignore identifiers nested in other words; before, something like "itp_" would incorrectly be converted to "itp." because "p_" is a reference. Now "itp_" and similar will be ignored while replacing "p_" references

	0.2b:

		* WRECKER will now replace all imports with a single "from compiler import *"
