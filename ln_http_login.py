#-*- coding:utf-8-*-

#calc sign

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


#post request

def post(url, data):
	import urllib2
	import urllib
	return urllib2.urlopen(urllib2.Request(url), urllib.urlencode(data)).read()


import time

def para_gen(mobile, password):
	para = {}
	para['mobile'] = mobile;
	para['password'] = password
	para['time'] = str(time.time())
	para['app_key'] = 'FKJ2whL69DJ+awKR/JmQ3123A=='
	para['role'] = '1'
	para['version'] = '1.0'
	para['sign'] = sign(para)
	return	para;

#测试
ln_login_url = 'http://api.ln.51jiaxiaotong.com/jxtapi/user/login_ln.do'
mobile = '13811125476'
password = '1q2w3e4r'

response = post(ln_login_url, para_gen(mobile, password))
print response

