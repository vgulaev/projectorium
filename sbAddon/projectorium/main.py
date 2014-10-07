# -*- coding: utf-8 -*-
import sublime, sublime_plugin

import os
import platform
import codecs

def gether_text( path ):
	if (platform.system() == "Windows"):
		dirsym = "\\"
	else:
		dirsym = "/"

	#path = __file__.split(dirsym)
	rootdir = path
	#rootdir = "C:\\Users\\Valentin\\workspace\\projectorium"
	stat = {".css" : {}, ".js" : {}, ".py" : {}, ".html" : {}}
	alllines = []
	for root, subFolders, files in os.walk(rootdir):
		for fl in files:
			fileName, fileExtension = os.path.splitext(fl)
			if root.find(dirsym + "libs" + dirsym) != -1:
				continue
			f = codecs.open(root + dirsym + fl, encoding="utf-8")
			if ((fileExtension in stat) == True):
				alllines.extend( f.readlines() )
			f.close()			
	return alllines

def clear_lines( one ):
	#clear white spases line
	for (i, e) in enumerate( one ):
		one[i] = one[i].strip()
	one.sort()

	while True:
		if one[0] == "":
			one.pop(0)
		else:
			break
	while True:
		if one[0][0]  == "#":
			one.pop(0)
		else:
			break
	simbol_for_wipe = "{}[].,+=():\\\"'!<>-/^?*|#:;`"
	for (i, e) in enumerate(one):
		for s in simbol_for_wipe:
			one[i] = one[i].lower().replace(s, " ")

def bild_vocabulary( one ):
	 sysv = set(["true", "false", "else", "self", "import", "class", "while", "pass"])
	 voc = set()
	 for e in one:
	 	tv = e.split( " " )
	 	voc |= set(tv)
	 voc ^= sysv
	 l = []
	 ns = set( ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] )
	 for e in voc:
	 	if ( len(e) > 3 ):
	 		if not(e[0] in ns):
	 			l += [e]
	 return l

def make_files( voc ):
	temp = """<snippet>
	<content><![CDATA[
{cont}
]]></content>
	<!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
	<tabTrigger>{cont}</tabTrigger>
	<!-- Optional: Set a scope to limit where the snippet will trigger -->
	<!-- <scope>source.python</scope> -->
</snippet>"""
	r = "c:\\Users\\Valentin\\AppData\\Roaming\\Sublime Text 3\\Packages\\User\\"
	for e in voc:
		fc = temp.format( cont = e )
		f = codecs.open(r + "pj-" + e + ".sublime-snippet", "w", encoding="utf-8" )
		f.write( fc )

def  delete_old_snipets():
	path = "c:\\Users\\Valentin\\AppData\\Roaming\\Sublime Text 3\\Packages\\User\\"
	for root, dirs, files in os.walk(path):
		for currentFile in files:
			#print "processing file: " + currentFile
			exts=('.sublime-snippet')
			if any(currentFile.lower().endswith(ext) for ext in exts):
				os.remove(os.path.join(root, currentFile))

project_root = "" 

class makesnipCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#self.view.insert( edit, 0, str( self.view.window().folders()[0] ) )
		alllines = gether_text( self.view.window().folders()[0] )
		clear_lines( alllines )
		voc = bild_vocabulary( alllines )
		delete_old_snipets()
		make_files( voc )
		#print voc
		#print len( voc )

if __name__ == '__main__':
	cmd = makesnipCommand()
	cmd.run(None)