######################################
#Parse kml and copy nested folders to separate files
#M.J. Churchill
#7/7/2014
#
########################################
import sys
import os

class gerror(Exception):
    def _get_message(self, message): return self._message
    def _set_message(self, message): self._message=message
    message=property(_get_message, _set_message)

def parsekml():
    try: 
        #---------------------------------
        #Get path to kml from user
        print "Previous files created with this utility will be overwritten."
        print "Path must be a valid .kml file. Unzip kmz files before using this utility"
        print "(Change ext. from .kmz to .zip and extract files as you would any other zip file"
        print " the result will be a folder with a doc.kml file in it)"
        print "Enter path to kml file:"
        filepath = raw_input('-->')
        f = open(filepath, 'r')

        #--------------------------------
        #Get path to destination folder from user
        print "Please enter path to destination folder:"
        dpath = raw_input('-->')
        
        
        #---------------------------
        #Variable declaration/initialization
        foldercount=0
        endfoldercount=0
        folderlevels=0
        checkline="n"
        

        #-------------------------
        # begin searching kml file for nested folders
        while checkline != '':
            #------------------------
            #start reading kml
            checkline = f.readline()
            #----------------------------------
            #check for "<Folder>"
            if "<Folder>" in checkline:

                #---------------------------------
                # increment count of '<Folder>' tags found
                # and calculate level of 'nesting'
                foldercount=foldercount+1
                level=foldercount-endfoldercount

                #------------------------------
                #Call function [folderfound] to write folder contents to file
                endfoldercount=folderfound(level, endfoldercount,f,dpath)
                
        f.close()
        
    except gerror as e:
        print "Error!: " & e.message
#--------------------------------------
# Function to write folder contents to file
def folderfound(level,endcnt,f,dpath):

    #---------------------------
    #Check level of folder nesting
    # (Function exits if not 2)
    if level <2:
        return endcnt
    elif level >2:
        return endcnt
    elif level ==2:
        checkline = f.readline()
        #-------------------------
        # The name tag must be the line following the folder tag
        # This may not always be true?
        if "<name>" in checkline:
            #-------------------------------
            #Extract the folder name from the read line
            nindex=checkline.index('<name>')
            eindex = checkline.index('</name>')
            thename = checkline[nindex+6:eindex]
            #------------------------------
            #Use the folder name to create the file name
            thename = thename.strip()
            newfilename = thename.replace(' ','_') + ".kml"

            #------------------------------
            #print file names to standard output
            print "   " + newfilename

            #--------------------------------------
            #Open file in destination folder and write contents
            writefile=open(dpath + newfilename,"w")
            writefile.write(r"""<?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
    <Document>
    <name>thename</name>
    """)
            writefile.write("<Folder>")
            writefile.write("<name>" + thename + "</name>")

        #-----------------------------
        #check for end of folder/file
        #Note: end of file should never be reached here if kml is valid
        while not "</Folder>" in checkline and checkline !='':
            checkline = f.readline()
            writefile.write(checkline)

        #--------------------------
        #count </Folder> tags reached
        endcnt=endcnt+1

        #---------------------------
        #Write closing tags in kml file
        writefile.write("</Document>")
        writefile.write("</kml>")
        writefile.close()

        return endcnt

if __name__ =='__main__':
    parsekml()
