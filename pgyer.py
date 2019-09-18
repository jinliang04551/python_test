#!/usr/bin/python
#*--coding=utf-8--*

import time
import sys
import urllib2
import urllib


#parse json
def parse_json(string, app_type):
	import json
	data = json.loads(string)['data']
	out  = ' ' + data['appName'] + ' ' + app_type + ' Beta V' + data['appVersion'] + ' build ' + data['appBuildVersion'] 
	out += '\n'
	out += ' ' + 'http://www.pgyer.com/' + data['appShortcutUrl']
	return out;

#判断是否有上传文件
if len(sys.argv) == 1:
   print '请输入上传文件路径'
   exit(1)

boundary = '----------%s' % hex(int(time.time() * 1000))
data = []


# 	# local response=`curl -# -F "file=@$1" -F "uKey=${u_key}" -F "_api_key=${api_key}" -F "publishRange=2" ${url}`

ukey='561cf63aa74205f812b02316f60326da'
api_key='a76ad5d2502ad599d454c8f601bfb321'

#append ukey
data.append('--%s\r\n' % boundary)
data.append('Content-Disposition: form-data; name="uKey"\r\n\r\n')
data.append(ukey)
data.append('\r\n')

# #append _api_key
# data.append(boundary)
# data.append('Content-Disposition: form-data; name="_api_key"\r\n')
# data.append(api_key)
# data.append(boundary)

data.append('--%s\r\n' % boundary)
data.append('Content-Disposition: form-data; name="_api_key"\r\n\r\n')
data.append(api_key)
data.append('\r\n')


# #append publishRange
# data.append('Content-Disposition: form-data; name="publishRange"\r\n')
# data.append('2')
# data.append(boundary)

data.append('--%s\r\n' % boundary)
data.append('Content-Disposition: form-data; name="publishRange"\r\n\r\n')
data.append('2')
data.append('\r\n')


file = sys.argv[1]
fr=open(file,'rb')

# data.append(fr.read())
# data.append('Content-Disposition: multipart/form-data; name="img_1"; filename="image_1.png"')
# data.append('Content-Type: %s\r\n' % 'image/png')
# data.append(fr.read())
# data.append(boundary)

data.append('--%s\r\n' % boundary)
data.append('Content-Disposition: form-data; name="file"; filename="%s"\r\n' % file)
data.append('Content-Type: application/octet-stream\r\n')
data.append('Content-Transfer-Encoding: binary\r\n\r\n')
data.append(fr.read())
fr.close()
data.append('\r\n')


data.append('--%s--' % boundary)


http_url='https://www.pgyer.com/apiv1/app/upload'
http_body=''.join(data)

req=urllib2.Request(http_url,data=http_body)
#header
req.add_header('Content-Type', 'multipart/form-data; charset=utf-8; boundary=%s' % boundary)
req.add_header('Content-Length', len(http_body))


#post data to server
resp = urllib2.urlopen(req, timeout=5)
#get response
response=resp.read()
print '==============================='
print parse_json(response,'')
print '==============================='







