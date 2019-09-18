#!/usr/bin/python
#-*-coding=utf-8-*-


import socket
import string
from struct import *


def getLength(para):
	l, = unpack('!I',para)
	return l

s  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('10.8.66.209',3000))
s.listen(5)


print 'listening .....'

conn , addr = s.accept()
print 'Connectted by' ,addr
print "a client have connected..."


try:
	print 'read data'
	header = conn.recv(4)

	# headerS = header.replace('\x','')
	# print headerS
	# print repr(headerS)


	# length = int(headerS,16)
	# print length 
	# print type(length)
	# print repr(length)

	fileLen = getLength(header)
	print fileLen

	# data = conn.recv(192651-4)
	data = conn.recv(fileLen)
	f = open('1.png','wb')
	f.write(data)

except socket.timeout:
	print 'socket.timeout'
finally:
	pass
	

conn.close()
s.close()