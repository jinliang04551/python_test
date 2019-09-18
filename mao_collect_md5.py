#-*- coding:utf-8-*-

#测试JXT-HTTP请求的脚本

#Author:毛可兵
#Date: 2016/05/27

import socket
import struct
import binascii
# import ASPIMPush_pb2
import aspire_aes_crypt
import threading
import sys

keys =[0x23,0x68,0x2a,0x91,0x5d,0x11,0xeb,0x9c,0x9f,0x08,0x2b,0x89,0xb6,0x80,0x6f,0x3a]
ivs = [0x1b,0xd8,0x06,0x50,0x22,0x38,0xba,0xf5,0x0f,0x07,0x0b,0xb5,0x9f,0xfa,0x9f,0xb7]

def get_hex(values):
	output = b''
	for x in xrange(0,len(values)):
		output +=struct.pack('B', values[x])
	return output	


aes_key = get_hex(keys)
aes_iv 	= get_hex(ivs)


print 'aes_key = ', binascii.b2a_hex(aes_key) 	
print 'aes_iv = ', binascii.b2a_hex(aes_iv) 	

#check------
#13466531630 aes->
#0xd4,0x7c,0x58,0xe5,0x96,0x85,0x77,0x64,0xaf,0x8c,0x7b,0xbf,0x7b,0x39,0xdc,0x85,
#->base64->1HxY5ZaFd2SvjHu/eznchQ==
#->md5->0347ace658346c29818ff02d16f23822

def md5(string):
    import hashlib
    m = hashlib.md5()   
    m.update(string)
    return m.hexdigest()

def aes_encrypt(text):
	aes = aspire_aes_crypt.AESCrypt(aes_key, aes_iv)
	return aes.encrypt(text)	

def aes_decrypt(text):
	aes = aspire_aes_crypt.AESCrypt(aes_key, aes_iv)
	return aes.decrypt(text)

def base64(text):
	import base64
	return base64.b64encode(text)

def gen_str(moblie):
	return md5(base64(aes_encrypt(moblie)))




#test
# print gen_str('13466531630')

#now doing 



# f = open('userids.csv', 'r')
# ids_string = f.read()
# ids = ids_string.split('\r\n')
# f.close()


# f = open('usermobile.csv', 'r')
# mobiles_string = f.read()
# f.close()
# mobiles = mobiles_string.split('\n')

# output = '';
# length = len(mobiles)
# info_dict = {}
# for x in xrange(0,length):
# 	m = mobiles[x]
# 	v = gen_str(m)
# 	info_dict[v] = m
# 	output += '%s,%s' % (m, v)
# 	output += '\r\n'

# # print info_dict


# f = open('values.csv', 'w')
# f.write(output)
# f.close()


# output = '';
# notfind = '';
# for x in xrange(0,len(ids)):
# 	m = ids[x]
# 	try:
# 		v = info_dict[m]
# 		print v
# 		output += '%s,%s' % (m, v)
# 		output += '\r\n'	
# 	except Exception, e:
		
# f = open('find.csv', 'w')
# f.write(output)
# f.close()

# md5_mobile
# f = open('20161227.csv')
# mobilesString = f.read()
# mobiles = mobilesString.split('\n')
# print mobiles 


# text = ''
# for mobile in mobiles:
# 	mobile_md5 =  gen_str(mobile)
# 	text += '%s,%s' %(mobile,mobile_md5)
# 	text += '\n'

# f = open('20161227_out.csv','w')
# f.write(text)
# f.close()


f = open('20161227.csv')
mobilesString = f.read()
mobiles = mobilesString.split('\n')
print mobiles 


text = ''
for mobile in mobiles:
	mobileIndex = mobile.find(",") + 1
	mobile = mobile[mobileIndex:-1]
	print mobile

	mobile_md5 =  gen_str(mobile)
	text += '%s,%s' %(mobile,mobile_md5)
	text += '\n'

f = open('20161227_out.csv','w')
f.write(text)
f.close()

# mobile_md5 = gen_str("13842667912")
# print mobile_md5
