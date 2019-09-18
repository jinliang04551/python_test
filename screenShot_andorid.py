#!/usr/bin/python
#*-----encoding=utf8-----*

import time

def getFileName():
	return time.gmtime

def screenshot():
	'adb shell /system/bin/screencap -p /sdcard/%s_screenshot.png',getFileName()

cmd_string = 'adb pull /sdcard/screenshot.png  /Users/liu/Desktop/%s_screenshot.png'


