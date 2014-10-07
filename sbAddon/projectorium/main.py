# -*- coding: utf-8 -*-
#import sublime, sublime_plugin

import os
import platform
import codecs

def gether_text():
	if (platform.system() == "Windows"):
		dirsym = "\\"
	else:
		dirsym = "/"

	#path = __file__.split(dirsym)
	rootdir = "C:\\Users\\Valentin\\workspace\\projectorium"
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
		if one[0][0] == "#":
			one.pop(0)
		else:
			break
	simbol_for_wipe = "{}[].,+=():\\\"'!<>-/^"
	for (i, e) in enumerate(one):
		for s in simbol_for_wipe:
			one[i] = one[i].lower().replace(s, " ")

def bild_vocabulary( one ):
	 sysv = set(["true", "false", "else", "self", "import", "class"])
	 voc = set()
	 for e in one:
	 	tv = e.split( " " )
	 	voc |= set(tv)
	 voc ^= sysv
	 l = []
	 for e in voc:
	 	if len(e) > 3:
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

#class makesnipCommand(sublime_plugin.TextCommand):

project_root = "" 
class makesnipCommand():
	def run(self, edit):
		print "Hello!!!"
		#self.view.insert(edit, 0, "Hello, Worlddfdff!")

alllines = gether_text()
clear_lines( alllines )
voc = bild_vocabulary( alllines )
make_files( voc )

print voc
print len( voc )