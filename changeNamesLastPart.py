#!/usr/bin/python
__author__ = 'Carlos A. Molina - @CarlosAMoli'

import sys
import os
scriptPath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(scriptPath+'/otherFunctions') # add folder to path to use its functions
from otherFunctions import *
from pyCheckFileORFolderExists import pyCheckFileORFolderExists
from pyDeleteCommasPath import pyDeleteCommasPath
from pyGetArchivesNameInPath import pyGetArchivesNameInPath
from pyGetFilesNameInPath import pyGetFilesNameInPath
from pyRenameFilesLastCharacters import pyRenameFilesLastCharacters

########################################################################
# rename files name. Example: coche.PNG->coche.png
# change last part of the name of all files in a folder
########################################################################

# functions

def askFilesPath():
	filesPath = raw_input('Type complete route of the folder with the files (/../../..):\n>>> ')
	return filesPath

def askWhatChange():
	# ouput: list of two strings
	originalCharacters = raw_input('Type original characters to change:\n>>> ')
	newCharacters = raw_input('Type new characters:\n>>> ')
	return [originalCharacters, newCharacters] # example ['png', 'PNG']

def checkArchivesPathSyntax(archivesName):
	if archivesName == -1:
		print 'ERROR: images path invalid syntax'
		return -1
	else:
		return 1

def checkFolderNotEmpty(archivesName):
	if archivesName==[]:
		print 'ERROR: folder is empty, no files'
		return -1
	else:
		return 1

# main

filesPath=askFilesPath()
filesPath = pyDeleteCommasPath(filesPath)
if pyCheckFileORFolderExists(filesPath,None,'folder')==1:
	archivesName = pyGetArchivesNameInPath(filesPath) # list or -1
	pathSyntax=checkArchivesPathSyntax(archivesName)
	if pathSyntax == 1:
		if checkFolderNotEmpty(archivesName) == 1:
			filesName = pyGetFilesNameInPath(filesPath,archivesName)
			whatChange = askWhatChange() # list of two strings
			renameCompleted = pyRenameFilesLastCharacters(filesPath, filesName, whatChange)
			if renameCompleted == 1:
				print 'Completed'
else:
	print "ERROR: folder doesn't exist"