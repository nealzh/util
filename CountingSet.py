#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

class CountingSet(object):

    def __init__(self, capacity, unitSize=32):
        
        self.unitSize = unitSize
        self.capacity = capacity
        self.length = capacity
        
        if(capacity <= 0):
            raise Exception('capacity must be > 0')
        if(unitSize == 8):
            self.unitType = np.uint8
        elif(unitSize == 16):
            self.unitType = np.uint16
        elif(unitSize == 32):
            self.unitType = np.uint32
        elif(unitSize == 64):
            self.unitType = np.uint64
        else:
            raise Exception('unitSize is only allow 8,16,32,64.')

        self.fullMask = self.unitType(18446744073709551615 >> (64 - unitSize))
        
        pool = np.zeros(self.capacity, self.unitType)
        
        self.pool = pool

    def get(self, fromIndex, length=1):
        
        '''Returns a new CountingSet composed of counters from this CountingSet from fromIndex (inclusive) to toIndex (exclusive).'''

        if(length == 1):
            return getOne(fromIndex)
        
        if((fromIndex) + length > self.length):
            raise Exception('CountingSet out of index.')
        
        counters = []
        
        for index in range(fromIndex, fromIndex + length):
            counters.append(self.pool[index])
        return counters
        
    def getList(self, indexes):

        '''Returns the value of the counter with the specified indexes.'''

        counters = []
        
        for index in indexes:
            
            if(index >= self.length):
                raise Exception('CountingSet out of index.')
            counters.append(self.pool[index])
        return counters
    
    def getOne(self, index):
        
        '''Returns the value of the counter with the specified index.'''
        
        if(index >= self.length):
            raise Exception('CountingSet out of index.')
        
        return self.pool[index]

    def set(self, fromIndex, length=1, value=1):
        
        '''Sets the counters from the specified fromIndex (inclusive) to the specified toIndex (exclusive) to the specified value.'''
        
        if(fromIndex + length > self.length):
            raise Exception('CountingSet out of index.')
        
        if(length == 1):
            return setOne(fromIndex, value)

        unitType = self.unitType
        
        for i in range(fromIndex, fromIndex + length):
            self.pool[i] = unitType(value)

    def setList(self, indexes, value=1):
        
        '''Sets the counter at the specified indexes to the specified value.'''

        unitType = self.unitType
        for index in indexes:
            if(index >= self.length):
                raise Exception('CountingSet out of index.')
            self.pool[index] = unitType(value)

    def setOne(self, index, value=1):
        
        '''Sets the counter at the specified index to the specified value.'''
        
        if(index >= self.length):
            raise Exception('CountingSet out of index.')
        
        self.pool[index] = self.unitType(value)

    def add(self, fromIndex, length=1, value=1):

        '''add the counters from the specified fromIndex (inclusive) to the specified toIndex (exclusive) to the specified value.'''
        
        if(fromIndex + length > self.length):
            raise Exception('CountingSet out of index.')
        
        if(length == 1):
            return setOne(fromIndex, value)

        value = self.unitType(value)
        fullMask = self.fullMask
        
        for index in range(fromIndex, fromIndex + length):
            if((fullMask - self.pool[index]) < value):
                self.pool[index] = fullMask
            else:
                self.pool[index] = self.pool[index] + value
    
    def addList(self, indexes, value=1):
        
        '''add the counters at the specified indexes to the specified value.'''

        value = self.unitType(value)

        fullMask = self.fullMask
        
        for index in indexes:
            if(index >= self.length):
                raise Exception('CountingSet out of index.')
            if((fullMask - self.pool[index]) < value):
                self.pool[index] = fullMask
            else:
                self.pool[index] = self.pool[index] + value

    def addOne(self, index, value=1):
        
        '''add the counter at the specified index to the specified value.'''

        if(index >= self.length):
            raise Exception('CountingSet out of index.')
            
        value = self.unitType(value)

        fullMask = self.fullMask
        
        if((fullMask - self.pool[index]) < value):
            self.pool[index] = fullMask
        else:
            self.pool[index] = self.pool[index] + value

    def minus(self, fromIndex, length=1, value=1):

        '''minus the counters from the specified fromIndex (inclusive) to the specified toIndex (exclusive) to the specified value.'''
        
        if(fromIndex + length > self.length):
            raise Exception('CountingSet out of index.')
        
        if(length == 1):
            return setOne(fromIndex, value)

        value = self.unitType(value)
        
        for index in range(fromIndex, fromIndex + length):
            if(index >= self.length):
                raise Exception('CountingSet out of index.')
            if(self.pool[index] <= value):
                self.pool[index] = 0
            else:
                self.pool[index] = self.pool[index] - value
    
    def minusList(self, indexes, value=1):
        
        '''minus the counters at the specified indexes to the specified value.'''

        value = self.unitType(value)
        
        for index in indexes:
            if(index >= self.length):
                raise Exception('CountingSet out of index.')
            if(self.pool[index] <= value):
                self.pool[index] = 0
            else:
                self.pool[index] = self.pool[index] - value

    def minusOne(self, index, value=1):
        
        '''minus the counter at the specified index to the specified value.'''

        value = self.unitType(value)
        
        if(self.pool[index] <= value):
            self.pool[index] = 0
        else:
            self.pool[index] = self.pool[index] - value
        
    def nextSetCount(self, fromIndex, value=True):
        '''Returns the index of the first counter that is set to true that occurs on or after the specified starting index.'''
        self.set(fromIndex, self.length - fromIndex, value)
        
    def previousSetCount(self, fromIndex, value=True):
        '''Returns the index of the nearest counter that is set to true that occurs on or before the specified starting index.'''
        self.set(0, fromIndex - 1, value)

    def clear(self):
        
        '''Sets the counters from the specified fromIndex (inclusive) to the specified toIndex (exclusive) to false.'''

        pool = self.pool
        
        for i in range(self.capacity):
            pool[i] = 0
    
    def nextClearCount(self, fromIndex):
        
        '''Returns the index of the first counter that is set to false that occurs on or after the specified starting index.'''

        self.set(fromIndex, self.length - fromIndex, False)
        
    def previousClearCount(self, fromIndex):
        
        '''Returns the index of the nearest counter that is set to false that occurs on or before the specified starting index.'''

        self.set(0, fromIndex - 1, False)

    def length(self):
        '''Returns the "logical size" of this CountingSet: the index of the highest set counter in the CountingSet plus one.'''
        return self.length
    def cardinality(self):
        '''Returns the number of counters set to true in this CountingSet.'''
        return None
    def size(self):
        '''Returns the number of counters of space actually in use by this CountingSet to represent counter values.'''
        return 0
    
    def isEmpty(self):
        
        '''Returns true if this CountingSet contains no counters that are set to true.'''

        b = False

        for i in range(self.capacity):
            b = b | (self.pool[i] > 0)
        
        return b
