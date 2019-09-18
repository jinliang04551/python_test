#!/usr/bin/python2.7
#*-----encoding=utf8-----*
# fib
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n + 1

for n in fib(6):
    print(n)


print('杨辉三角')
print('=====================================')
print('=====================================')
print('=====================================')

def triangles():
    n = [1]
    while True:
        yield n
        s = n[:]
        s.append(0)
        n = [s[i-1] + s[i] for i in range(len(s))]

# def triangles():
#     n = [1]
#     while True:
#         yield n
#         # s = n[:]
#         n.append(0)
#         n = [n[i-1] + n[i] for i in range(len(n))]


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')



from functools import reduce
def fn(x,y):
    return x * 10 + y
f = reduce(fn,[1,3,5,7,9])


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

num = reduce(fn,map(char2num,'13579'))
print(num)


# def char2float(s):
#     num = reduce(fn,map(char2num,s))
#     print num
#     i = s.find('.')
#     if i > 0:
#         sb = s[i:-1]
#         print sb
#         num = num * 10 * (sb -1) *(-1)
#         print num
#     return num

# s1 = char2float('0.22331')
# s2 = char2float('123445')
# s3 = char2float('12344.9055')

# print('s1:%f'%s1)
# print(s2)
# print(s3)


def str2float(s):
    index = s.find('.')
    def f1(x,y):
        return x * 10 + y
    def f2(x,y):
        return x/10 + y

    s1 = reduce(f1,map(int,s[:index]))
    s2 = reduce(f2,map(int,s[index + 1:]))*0.1

    return s1 + s2

s1 = str2float('123.021')
s2 = str2float('0.223')
s3 = str2float('12333')
s4 = str2float('00001.233')

print('s1:%f\ns2:%f\ns3:%f\ns4:%f\n' %(s1,s2,s3,s4))


#装饰器
def log(func):
    def wrapper(*args,**kw):
        print('call %s()' %func.__name__)
        return func(*args,**kw)
    return wrapper

@log

def now():
    print('2015-3-25')

now()

