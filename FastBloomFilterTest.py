#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from FastBloomFilter import FastBloomFilter

ISOTIMEFORMAT = '%Y-%m-%d %X'

n = 1000000
fpr = 0.0001
t = 800000

print('start BloomFilter test.')
print()
print('size:', n)

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start create BitSet.')
bf = FastBloomFilter(n, fpr)
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end create BitSet.')

print('m: ', bf.m, 'n: ', bf.n, 'k: ', bf.k)

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start add.')
start = time.time()
for i in range(t):
	bf.append(str(i))
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end add.')
print('totail time: ', end - start, ' seconds.')
print(t / (end * 1000 - start * 1000) , ' times add per ms.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start exists.')
start = time.time()
for i in range(t):
    bf.exists(str(i))
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end exists.')
print('totail time: ', end - start, ' seconds.')
print(t / (end * 1000 - start * 1000) , ' times exists per ms.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start error.')
errorCount = 0
for i in range(n * 10):
    if(i < t):
        if(not bf.exists(str(i))):
            errorCount = errorCount + 1
    else:
        if(bf.exists(str(i))):
            errorCount = errorCount + 1
    if(i !=0 and i % 10000 == 0):
        print(i, ' times tests found ', errorCount, ' error. ', 'error rate: ', errorCount / i)
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end error.')
print('test ', n * 10, ' times', ' error times: ', errorCount)
print('error rate: ', errorCount / (n * 10))

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start remove.')
start = time.time()
for i in range(n):
    bf.remove(str(i))
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end remove.')
print('totail time: ', end - start, ' seconds.')
print(n / (end * 1000 - start * 1000) , ' times remove per ms.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start clear.')
start = time.time()
bf.clear()
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end clear.')
print('totail time: ', end - start, ' seconds.')
print(t / (end * 1000 - start * 1000) , ' times clear per ms.')
