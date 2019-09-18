#-*- coding:utf-8-*-

#author Maokebing

#指定apk文件
parent_apk='/Users/Mao/WorkSpace/Python/1.ipa'
teacher_apk='/Users/Mao/WorkSpace/Python/1.ipa'


#上传 apk 到蒲公英
def upload_to_pgyer(app_type, apk_file):
	import os
	print app_type + u' 正在上传...'
	u_key='561cf63aa74205f812b02316f60326da'
	api_key='a76ad5d2502ad599d454c8f601bfb321'
	url='http://www.pgyer.com/apiv1/app/upload'
	curl_cmd  = 'curl -F "file=@%s" -F "uKey=%s" -F "_api_key=%s" -F "publishRange=2" %s' % (apk_file, u_key, api_key, url)
	out = os.popen(curl_cmd, 'r').read()
	return out

#解析返回的json
def parse_json(string, app_type):
	import json
	data = json.loads(string)['data']
	out  = ' ' + data['appName'] + ' ' + app_type + ' Beta V' + data['appVersion'] + ' build ' + data['appBuildVersion'] 
	out += '\n'
	out += ' ' + u'下载地址: ' + 'http://www.pgyer.com/' + data['appShortcutUrl']
	return out;

#上传开始
res1 = upload_to_pgyer(u'家长版', parent_apk)
res2 = upload_to_pgyer(u'老师版', teacher_apk)

#输出
out  = '\n'
out += u' ** 上传成功! ** '
out += '\n'
out += '========================================'
out += '\n'
out += parse_json(res1, u'家长版')
out += '\n'
out += parse_json(res2, u'老师版')
out += '\n'
out += '========================================'

print out


