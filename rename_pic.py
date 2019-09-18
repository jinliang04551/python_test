#!/usr/bin/python
#*-----encoding=utf8-----*
import sys

def rename_pic(name):
	firstC = name[0].lower()
	outname = firstC
	for i in range(1,len(name)):
		c = name[i]
		prefix = '_'
		if c == '_':
			outname +=c
		elif c.isupper():
			c=c.lower()
			outname +=prefix
			outname +=c
		else:
	 		outname +=c
	print outname 

		

if len(sys.argv) == 1:
   print '请输入文件名'
   exit(1)

filename = sys.argv[1]
rename_pic(filename)