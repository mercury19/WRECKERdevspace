# WRECKER-1.1


What it does:

	* Go through any specified files and change all specified native references to WRECK dynamic references.
	* This only applies for static references. fac_kingdom_6 will be changed to fac.kingdom_6, while quoted references like "fac_kingdom_6" will be left as is.
	* Ignore references in the middle of constants, script names, etc., "create_mesh_overlay" for example.
	* Access files in a subdirectory if you want to change some old files that have quoted references to dynamic ones, for example.
	* Replace all imports with a single "from compiler import *"
	* Ignore identifiers at the end of words, spt_ vs pt_ for example. pt_ is the party_templates identifier, which we want to change, while spt_ is a constant, which we don't want to change.
	* Fix imports in header files.




INSTALLATION:
	
	1) Download one of the two "WRECKER" files. You don't need both, just choose one. 
		a) If you want to, download the matching .bat file. There's really no reason not too but it's technically optional. 

	2) Put the "WRECKER" file (and .bat if you have it) in the same folder as your "module_" files. Boom. Installed.

	3) Make sure you compile using WRECK. If you try to use this program with the native compiler you will be drowned errors. 


USE:

	1) Run the program. Its easiest to do this using the .bat, but if you don't want to use it you can also just run it with python. If you do it this way, make sure that all ".py" files are set to open with python as the default program. It won't work otherwise.
		a) To set files for the program to WRECK, open up "WRECKER" in a text editor and find "files_to_process". It should be near the top. Add your the files you want to run, without the file extensions. Follow the examples already there. 

	2) If you downloaded the regular version, follow the on-screen menu. If not, watch it run. All done. 

Questions, comments, bugs, and source code:

	* All questions, comments, and bug reports can be sent to mercury19 on the taleworlds forums, or posted in the WRECK thread, here: https://forums.taleworlds.com/index.php/topic,325102.0.html
	* If you want to work on WRECKER, go for it. You can request a pull from here, or just download the source folder and go to town. The source code is Native 1.171. I did not inlcude WRECK because I didn't find it necessary for creating WRECKER. I use wreckertesting.py for testing new ideas, and then copy the necessary code into wrecker.py, but you can do what you want. If you add stuff let me know so I can check it out, and possibly use your better version :P

Also, go ahead and ignore the sublime files~


CHANGELOG:

	1.1:

		* ACTUAL full functionality. 100% tested on native
		* Added function for fixing header imports, since many referenced ID files which WRECK doesn't need
		* Finalized lists of prefixes to be changed and files to fix. Unused prefixes/files are noted above their respective lists
		* Improved import replacement method

		* Fixed a bug causing the import fixer to remove the "factions = [" in module_factions

		* Removed support for quoted reference replacement. Consistency is nice, but it caused too many errors to be worth it.
		* Removed support for string reference replacements. All string references are quoted, and many HAVE to be quoted because they contain special characters that mess with the compiler otherwise.

	1.0:

		* Added support for changing string references
		* WRECKER options are now added to module_info.py by default

		* Fixed bug where if an identifier had a static reference followed by a quoted reference, the quoted reference was not properly processed

		* Cleaned code for determining identifiers - 1 dict and 2 lists rather than multiple of both
		

	0.3b:

		* Wrecker will now ignore identifiers nested in other words; before, something like "itp_" would incorrectly be converted to "itp." because "p_" is a reference. Now "itp_" and similar will be ignored while replacing "p_" references

	0.2b:

		* WRECKER will now replace all imports with a single "from compiler import *"
