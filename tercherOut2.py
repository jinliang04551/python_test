#! /usr/bin/python
# -*-coding=utf-8-*-
# author liu

import re

def gen_key(data):
	valueOut = ''
	for item in data:
		if item == '':
			pass
		elif item.find('=') >0:
			subIndex =  item.find('=')
			value = item[subIndex:].strip()

			key = value.strip(' =;"')
			keyList = key.split('_')
			key = 'extern NSString *  MISUM'
			event = ''
			for keyword in keyList:
				key += keyword.title()

			event += key
			event += ';'
			event += '\t\n'
			valueOut += event
		else:
			valueOut +=  item
			valueOut +=  '\n'

	print valueOut
	return valueOut

def key2File(context):
	with open('ynUMKey.h','w') as f:
		f.write(context)

def gen_value(data):
	valueOut = ''
	for item in data:
		if item == '':
			pass
		elif item.find('=') >0:
			subIndex =  item.find('=')
			value = item[subIndex:].strip()
			value = value.replace('= ','= @')

			key = value.strip(' @=;"')
			keyList = key.split('_')
			key = 'NSString *  MISUM'
			event = ''
			for keyword in keyList:
				key += keyword.title()

			event += key
			event += '\t'
			event += value
			event += '\n'
			valueOut += event
		else:
			valueOut +=  item
			valueOut +=  '\n'

	print valueOut
	return valueOut

def value2file(context):
	with open('ynUMKey.m','w') as f:
		f.write(context)


with open('11.txt') as f:
	string = f.read()
	L = string.split('\n')

	key2File(gen_key(L))
	value2file(gen_value(L))

