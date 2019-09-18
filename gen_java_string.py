#-*-encoding=utf-8-*-

#author:maokebing

s = open('umeng_event02-teacher.txt', 'rw');
s1 = s.read()

#按换行分割
l = s1.split('\n')

#生成
out = ''
for x in l:
	y=x.split(',')
	if len(y) == 3:
		v = y[0] #值
		c = y[1] #注释
		line = '// '+ c + '\n' + 'public static final String ' + v.upper() + ' = ' + '"' + v + '";\n\n'
		out += line


print out

s.close()

#写入文件
f = file('teacher.txt', 'w')
f.write(out)
f.close()