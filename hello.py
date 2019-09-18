#!/usr/bin/python2.7
#*-----encoding=utf8-----*

__author__ = 'liujinliang'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('hello,world')
    elif len(args) == 2:
        print('hello,%s'%args[1])
    else:
        print('too many argument')

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
        
class Hello(object):
    def hello(self,name='world'):
        print('Hello,%s.' %name)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a


    

if __name__ == '__main__':
    test()
    for n in Fib():
        print(n)

