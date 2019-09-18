#!/usr/bin/python
#-*-coding=utf-8-*-


import socket
import struct 
import sys
import time 

#建立socket连接，并设置为自动重用的
s  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)    

#绑定地址，端口，监听请求
s.bind(('172.20.10.3',3000))
s.listen(5)
print 'listening .....'

#已连接请求
conn , addr = s.accept()
print 'Connectted by' ,addr

#解析开始的4字节，得到数据内容长度
fileLengthBuffer = conn.recv(4)
print fileLengthBuffer
fileDataLength, = struct.unpack("!I",fileLengthBuffer)
print 'fileDataLength:', fileDataLength

#定义一次接受数据最大长度
maxLength = 1024

#阻塞式接收数据
buffer = ''
buf    = ''
remainDataLength = fileDataLength

while True:
    try:
    	if remainDataLength < maxLength:
    		buf = conn.recv(remainDataLength)
    		remainDataLength -= remainDataLength
    	else:
    		buf = conn.recv(maxLength)
	        remainDataLength -= maxLength

    except socket.error as err_msg:
    	print 'recv data before error', buffer
        print('Error receiving data: %s' %err_msg)
        sys.exit(1)
    # if not len(buf):
    #     break 
    # buffer += buf
    buffer += buf


    if remainDataLength:
       pass
    else:
    	break
      
    # print 'recv data :%s' %buffer
        
# print 'recv all data :%s' %buffer
print 'recv all data Length :%d' %len(buffer)


#保存文件
timeFormatString = time.strftime('%Y%m%d%H:%M:%S',time.localtime(time.time()))
f = open('./%s' %timeFormatString,'wb')
f.write(buffer)
f.close()
print 'write to file finished'
conn.close()

