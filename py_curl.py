#!/usr/bin/python
#*-----encoding=utf8-----*

def sign(para):
	import hmac
	import base64
	import hashlib
	l = []
	for x in sorted(para.keys()):
		l.append('%s=%s' % (x, para[x]))
	s = '&'.join(l)	
	key = '*+*Aspire*+*'
	return base64.b64encode(hmac.new(key, s, hashlib.sha1).digest())


def para_gen():
	para = {}
	para['userId']  = '54828668'
	para['app_key'] = 'rdmH9vHZ23S3xvRaWctldQ=='
	para['version'] = '3.0'
	para['time']    = str(time.time())
	para['sign']    = sign(para)
	print 'para:%s' %para
	return para


#上传至pgyer
def upload(): 
	http_url='http://file.api.yn.51jiaxiaotong.com/andedu-file/upload/uploadFile'
    
    curlString = 'curl -# -F \"file=@$1\"'
    for key,value in para_gen().items():
    	curlString += '-F '
    	curlString += '\"%s='  %key
    	curlString += '${%s}' %value
    curlString += '${%s}' %http_url
	
	print 'curlString:%s' %curlString

	if [ $? -ne 0 ];then
		echo_red "** 上传失败. **"
        exit 1 
    fi
	
	echo ${response}

upload()

