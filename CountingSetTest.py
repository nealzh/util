#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from CountingSet import CountingSet

ISOTIMEFORMAT = '%Y-%m-%d %X'

cap = 10000000
size = 32
listSize = 8
indexes = [1, 555, 687987, 73521, 53821, 1287, 36746, 2165]

n = 100

print('start CountingSet test.')
print()
print('cap:', cap, '; size:', size)

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start create CountingSet.')
bs = CountingSet(cap, size)
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end create CountingSet.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start setOne.')
start = time.time()
for i in range(cap):
	bs.setOne(i, n)
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end setOne.')
print('totail time: ', end - start, ' seconds.')
print(cap / (end * 1000 - start * 1000) , ' times setOne per ms.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start setList.')
start = time.time()
for i in range(int(cap / listSize)):
	bs.setList(indexes, n)
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end setList.')
print('totail time: ', end - start, ' seconds.')
print(cap / (end * 1000 - start * 1000) , ' times setList per ms.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start set.')
start = time.time()
bs.set(0, cap, n)
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end set.')
print('totail time: ', end - start, ' seconds.')
print(cap / (end * 1000 - start * 1000) , ' times set per ms.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start getOne.')
start = time.time()
for i in range(cap):
	bit = bs.getOne(i)
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end getOne.')
print('totail time: ', end - start, ' seconds.')
print(cap / (end * 1000 - start * 1000) , ' times getOne per ms.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start getList.')
start = time.time()
for i in range(int(cap / listSize)):
	bits = bs.getList(indexes)
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end getList.')
print('totail time: ', end - start, ' seconds.')
print(cap / (end * 1000 - start * 1000) , ' times getList per ms.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start get.')
start = time.time()
bits = bs.get(0, cap)	
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end get.')
print('totail time: ', end - start, ' seconds.')
print(cap / (end * 1000 - start * 1000) , ' times get per ms.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start addOne.')
start = time.time()
for i in range(cap):
	bit = bs.addOne(i, n)
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end addOne.')
print('totail time: ', end - start, ' seconds.')
print(cap / (end * 1000 - start * 1000) , ' times addOne per ms.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start addList.')
start = time.time()
for i in range(int(cap / listSize)):
	bits = bs.addList(indexes, n)
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end addList.')
print('totail time: ', end - start, ' seconds.')
print((cap * size) / (end * 1000 - start * 1000) , ' times addList per ms.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start add.')
start = time.time()
bits = bs.add(0, cap, n)	
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end add.')
print('totail time: ', end - start, ' seconds.')
print((cap * size) / (end * 1000 - start * 1000) , ' times add per ms.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start minusOne.')
start = time.time()
for i in range(cap):
	bit = bs.minusOne(i, 2)
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end minusOne.')
print('totail time: ', end - start, ' seconds.')
print((cap * size) / (end * 1000 - start * 1000) , ' times minusOne per ms.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start minusList.')
start = time.time()
for i in range(int(cap / listSize)):
	bits = bs.minusList(indexes, 2)
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end minusList.')
print('totail time: ', end - start, ' seconds.')
print((cap * size) / (end * 1000 - start * 1000) , ' times minusList per ms.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start minus.')
start = time.time()
bits = bs.minus(0, cap, 2)	
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end minus.')
print('totail time: ', end - start, ' seconds.')
print((cap * size) / (end * 1000 - start * 1000) , ' times minus per ms.')


print()

import cProfile

cProfile.run("bs.setOne(0)")
