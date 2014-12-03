Extract KML Folders
==========

_parsekml.py_ is a Python script to extract subfolders from a kml file  
_doc.kml_ is the kml file created in Google Earth used to test the Python script

Each subfolder in the .kml file is written to a separate file. The file name will be the folder name with leading and trailing spaces stripped and internal spaces replaced with underscores

Fixes needed:
-------------
1. Make the code more elegant and robust:
  - exit gracefully if file is not valid kml or if .kmz file is given
  - exit gracefully if destination path is not valid
  - recognize if destination path is given with or without trailing backslash and act accordingly. (Currently, **not** including the backslash at the end will result in the files being saved to the wrong location, with the wrong name.) 
  - Add a check to see if the 'name' tag exists in the line after the 'folder' tag. Currently the 'name' tag **must** be in the line following the 'Folder' tag or the script will fail.
  - Add check that readline() did not return more than one trigger (e.g. the 'Folder' and 'name' tags in the same line).

2. Add recursivity (currently the script will only work if there is a single level of nesting)
  For example, consider the following folder structure:

          Top level folder (Level 1)
                      |
                folder within top level folder (Level 2)
                              |
                        Folder in that folder (Level 3)
            
            
  The script will fail because it will end the file at the end of the 'Level 3' folder instead of extracting it to a separate file and continuing with the 'Level 2' folder.
  
3. Add check for duplicate folder names (currently, if there are multiple folders with the same name, the existing file will be overwritten.)
  
4. Add ability to deal with features in the 'Level 1' folder (features not in subfolders)

5. Create a GUI (Tkl?) and deployable package

6. Include styles in output file. Currently the 'StyleMap' section of the original .kml file is dropped so symbology reverts to the defaults (e.g. yellow pushpin).
