#!/usr/bin/python
#*--coding=utf-8--*

import time
import sys
import urllib2
import urllib
import os

def parse_json(string, app_type):
	import json
	out = '' + json.loads(string)['errMsg'] + '\r\n'
	errCode = json.loads(string)['errCode']
	if int(errCode) == 0:
		data = json.loads(string)['data']
		for key in data:
			out += '%s : %s\r\n' %(key,data[key]) 
		return out
	return out;

def sign(para):
	import hmac
	import base64
	import hashlib
	l = []
	for x in sorted(para.keys()):
		l.append('%s=%s' % (x, para[x]))
	s = '&'.join(l)	
	key = '<#*+*Aspire*+*#>'
	return base64.b64encode(hmac.new(key, s, hashlib.sha1).digest())


def para_gen():
	para = {}
	para['userId']  = '54828668'
	para['app_key'] = 'rdmH9vHZ23S3xvRaWctldQ=='
	para['version'] = '3.0'
	para['time']    = str(time.time())
	para['sign']    = sign(para)
	return para

def appendParas(dic,data,boundary):
	for key,value in dic.items():
		data.append('--%s\r\n' % boundary)
		data.append('Content-Disposition: form-data; name="%s"\r\n\r\n' %key)
		data.append(value)
		data.append('\r\n')
	return data


def appendFile(boundary):
	outString = ''
	for i in range(1,len(sys.argv)):
		file = sys.argv[i]
		print ('index:%d file_path:%s' %(i,file))
		fr=open(file,'rb')
		string = '--%s\r\n' % boundary
		if file.find('amr') == -1:
			string += 'Content-Disposition: form-data; name="img_%i"; filename="image_%i.webp"\r\n' % (i,i)
			# string += 'Content-Disposition: form-data; name="audio"; filename="audio.amr"\r\n'
		else:			
			string += 'Content-Disposition: form-data; name="audio"; filename="audio.amr"\r\n'

		string += 'Content-Type: application/octet-stream\r\n'
		string += 'Content-Transfer-Encoding: binary\r\n\r\n'
		# print 'filename:%s string:%s' %(file,string)
		string += fr.read()
		string += '\r\n'
		fr.close()
		outString += string
	# print outString
	return outString


#判断是否有上传文件
if len(sys.argv) == 1:
   print '请输入上传文件路径'
   exit(1)


data = []
boundary='-------<2017_aspire>--------'

#添加参数
body = appendParas(para_gen(),data,boundary)
#添加文件

body.append(appendFile(boundary))
body.append('--%s--' % boundary)

# print 'body:%s' %body

http_url='http://file.api.yn.51jiaxiaotong.com/andedu-file/upload/uploadFile'
http_body=''.join(body)

try:
	#build http Request
	req=urllib2.Request(http_url,data=http_body)
	#header
	req.add_header('Content-Type', 'multipart/form-data; charset=utf-8; boundary=%s' %boundary)
	req.add_header('Content-Length', len(http_body))
	# req.add_header('User-Agent','Mozilla/5.0')
	# req.add_header('Referer','http://file.api.yn.51jiaxiaotong.com')
	#post data to server
	resp = urllib2.urlopen(req, timeout=5)
	#get response
	response=resp.read()
	print '==============================='
	print response

	print '==============================='
	print parse_json(response,'')
	print '==============================='

except Exception as e:
	raise e


	
