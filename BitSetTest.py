#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

ISOTIMEFORMAT = '%Y-%m-%d %X'

cap = 4000000
size = 8
listSize = 8
indexes = [1, 555, 687987, 73521, 53821, 1287, 36746, 2165]

print('start BitSet test.')
print()
print('cap:', cap, '; size:', size, '; bites:', cap * size)

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start create BitSet.')
bs = BitSet(cap, size)
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end create BitSet.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start setOne.')
start = time.time()
for i in range(cap * size):
	bs.setOne3(i, False)
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end setOne.')
print('totail time: ', end - start, ' seconds.')
print((cap * size) / (end * 1000 - start * 1000) , ' times setOne per ms.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start setList.')
start = time.time()
for i in range(int((cap * size) / listSize)):
	bs.setList(indexes, False)
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end setList.')
print('totail time: ', end - start, ' seconds.')
print((cap * size) / (end * 1000 - start * 1000) , ' times setList per ms.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start set.')
start = time.time()
bs.set3(0, cap * size)
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end set.')
print('totail time: ', end - start, ' seconds.')
print((cap * size) / (end * 1000 - start * 1000) , ' times set per ms.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start getOne.')
start = time.time()
for i in range(cap * size):
	bit = bs.getOne(i)
#bits = bs.get2(0, cap * size)	
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end getOne.')
print('totail time: ', end - start, ' seconds.')
print((cap * size) / (end * 1000 - start * 1000) , ' times getOne per ms.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start getList.')
start = time.time()
for i in range(int((cap * size) / listSize)):
	bits = bs.getList(indexes)
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end getList.')
print('totail time: ', end - start, ' seconds.')
print((cap * size) / (end * 1000 - start * 1000) , ' times getList per ms.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start get.')
start = time.time()
bits = bs.get2(0, cap * size)	
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end get.')
print('totail time: ', end - start, ' seconds.')
print((cap * size) / (end * 1000 - start * 1000) , ' times get per ms.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start flipOne.')
start = time.time()
for i in range(cap * size):
	bit = bs.flipOne(i)
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end flipOne.')
print('totail time: ', end - start, ' seconds.')
print((cap * size) / (end * 1000 - start * 1000) , ' times flipOne per ms.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start flip.')
start = time.time()
bits = bs.flip(0, cap * size)
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end flip.')
print('totail time: ', end - start, ' seconds.')
print((cap * size) / (end * 1000 - start * 1000) , ' times flip per ms.')

print()

import cProfile

cProfile.run("bs.setOne(0)")
