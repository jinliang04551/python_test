#!/usr/bin/python2.7
#*-----encoding=utf8-----*

import random
import sys

print(sys.argv)

if len(sys.argv) <= 1:
    print '缺少参数'
    sys.exit()

def ranstr(num):
    # 猜猜变量名为啥叫 H
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

    salt = ''
    for i in range(num):
        salt += random.choice(H)

    return salt

bitCount = int(sys.argv[1])
salt = ranstr(bitCount)
print salt
