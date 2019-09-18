#-*-encoding=utf-8-*-

#author:maokebing

s = open('umeng_event02-teacher.txt', 'rw');
s1 = s.read()

def set_str(string):
	l = list(string)
	out = ''
	l1 = len(l)
	l2 = []
	for x in xrange(1,l1):
		if l[x] == '_':
			l2.append(x)

	#驼峰		
	l[0] = l[0].upper()

	for x in l2:
		l[x+1] = l[x+1].upper()
		l[x] = '' 		

	out = ''.join(l)
	return out


#按换行分割
l = s1.split('\n')

#生成
out1 = ''
out2 = ''

for x in l:
	y=x.split(',')
	if len(y) == 3:
		v = y[0] #值
		c = y[1] #注释
		line1 = '// '+ c + '\n' + 'extern NSString *  MISUM' + set_str(v) + ';\n\n'
		out1 += line1
		line2 = '// '+ c + '\n' + 'NSString *  MISUM' + set_str(v) + ' = ' + '@"' + v + '";\n\n'
		out2 += line2


print out1
print out2

s.close()

out = out1 + '\n\n===================================\n\n' + out2

#写入文件
f = file('teacher_ios.h', 'w')
f.write(out)
f.close()

