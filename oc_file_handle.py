#!/usr/bin/python
#*--coding=utf-8--*

from sys import argv
import string

if len(argv) < 2:
	print "you need input a file"
	exit()
if len(argv) > 2:
	print "you input more than 2 parameter"
	exit()

f = open(argv[1],'r')
s1 = f.read()

# l = []
# for line in f:
# 	# print line
# 	if line.find('-') < 0:
# 	   print "not the function start."
# 	else:
# 	   print line
# 	   line

l = s1.split('-')
print l	
