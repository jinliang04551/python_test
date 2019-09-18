#!/usr/bin/python
#*---encoding=utf-8-------*

from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2

register_openers()

datagen,headers = multipart_encode({"image1":open("QQ20170512-153106.png","rb")})

http_url='http://file.api.yn.51jiaxiaotong.com/andedu-file/upload/uploadFile'

request = urllib2.request(http_url,datagen,headers)

print urllib2.urlopen(request).read()
