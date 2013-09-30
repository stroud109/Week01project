'''
open original_files folder
read individual file names
sort file names according to first letter, which will be lowercase
sort file names into directories a - z, which are inside alphabet_files folder
'''

#make folder for alphabet by using `mkdir {a..z}`

import os
import shutil
#magical modules

PATH_ROOT = "/Users/smstroud/Development/Week01project"
#this will help us write code to move files in a more manageable way

source_files_root = "%s/original_files/files" % PATH_ROOT
#tells us the original directory where our text files are located

dirs = os.listdir(source_files_root)
#lists out all the file names in the folder

for file_name in dirs:
	#print "file name is " , file_name --> this works because listdirs, as defined above, only gives you file names 
	#print  "first letter of file name is " , file_name[0:1]
	#print "file name type is " , type(file_name)

	first_letter = file_name[0] #first_letter applies to file_name, and eventually alphabet_files
	source_file_path = "%s/%s" % (source_files_root, file_name)
	#the individual text file is added to the source_files_root variable
	#defining this variable will help us copy the text file from a location
	destination_file_path = "%s/alphabet_files/%s/%s" % (PATH_ROOT, first_letter, file_name)
	#defining this variable will help us copy the text file to a new location

	#if first_letter == 'a':
		#print "first letter " , first_letter
	shutil.copyfile(source_file_path, destination_file_path)
	#this is a test --> print source_file_path, destination_file_path
	#copyfile is a function that's available in shutils
	#this is th point where we actually copy a text file to a new location
