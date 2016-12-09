#!/usr/bin/python
# -*- coding: utf-8 -*-

import array

class BitSet(object):
    
    def __init__(self, capacity, unitSize=32):
        
        self.unitSize = unitSize
        self.capacity = capacity
        self.length = unitSize * capacity
        
        if(capacity <= 0):
            raise Exception('capacity must be > 0')
        if(unitSize == 8):
            self.unitType = 'B'
        elif(unitSize == 16):
            self.unitType = 'H'
        elif(unitSize == 32):
            self.unitType = 'I'
        elif(unitSize == 64):
            self.unitType = 'Q'
        else:
            raise Exception('unitSize is only allow 8,16,32,64.')
        
	#fullMask = 0xffffffffffffffff
        self.fullMask = 18446744073709551615 >> (64 - unitSize)
        
        pool = array.array(self.unitType, [0])
        
        for i in range(capacity - 1):
            pool.append(0)
        
        self.pool = pool


    def get(self, fromIndex, length):
        
        '''Returns a new BitSet composed of bits from this BitSet from fromIndex (inclusive) to toIndex (exclusive).'''
        
        if((fromIndex) + length > self.length):
            raise Exception('BitSet out of index.')
        
        bucketIndex, unitIndex = divmod(fromIndex, self.unitSize)
        mask = 1 << unitIndex
        bits = []
        
        for i in range(length):
            if(i != 0 and (fromIndex + i) % self.unitSize == 0):
                bucketIndex = bucketIndex + 1
                mask = 1
                unitIndex = 0
            bits.append(((self.pool[bucketIndex] & mask) >> unitIndex) & 1)
            mask = mask << 1
            unitIndex = unitIndex + 1
        return bits
    
    def getOne(self, index):
        
        '''Returns the value of the bit with the specified index.'''
        
        #if(index >= self.length):
        #    raise Exception('BitSet out of index.')
        
        bucketIndex, unitIndex = divmod(index, self.unitSize)
        mask = 1 << unitIndex
        
        return ((self.pool[bucketIndex] & mask) >> unitIndex) & 1
    
    def set(self, fromIndex, length, value=True):
        
        '''Sets the bits from the specified fromIndex (inclusive) to the specified toIndex (exclusive) to the specified value.'''
        
        bucketIndex, unitIndex = divmod(fromIndex, self.unitSize)

        for i in range(length):
            if(i != 0 and (fromIndex + i) % self.unitSize == 0):
                bucketIndex = bucketIndex + 1
                unitIndex = 0
            head = (((self.pool[bucketIndex] >> (unitIndex + 1)) << 1) + value) << unitIndex
            #print(bin(head))
            tail = self.pool[bucketIndex] & (self.fullMask >> (self.unitSize - unitIndex))
            #print(bin(tail))
            self.pool[bucketIndex] = head | tail
            unitIndex = unitIndex + 1
        
        
    def setOne(self, index, value=True):
        
        '''Sets the bit at the specified index to the specified value.'''
        
        #if(index >= self.length):
        #    raise Exception('BitSet out of index.')
        
        bucketIndex, unitIndex = divmod(index, self.unitSize)
        #print(bin(self.pool[bucketIndex]))
        head = (((self.pool[bucketIndex] >> (unitIndex + 1)) << 1) + value) << unitIndex
        #print(bin(head))
        tail = self.pool[bucketIndex] & (self.fullMask >> (self.unitSize - unitIndex))
        #print(bin(tail))
        self.pool[bucketIndex] = head | tail
        #print(head | tail)
        
    def nextSetBit(self, fromIndex):
        '''Returns the index of the first bit that is set to true that occurs on or after the specified starting index.'''
        return 0
    def previousSetBit(self, fromIndex):
        '''Returns the index of the nearest bit that is set to true that occurs on or before the specified starting index.'''
        return 0
    def flip(self, fromIndex, length=1):
        '''Sets each bit from the specified fromIndex (inclusive) to the specified toIndex (exclusive) to the complement of its current value.'''
        return None

    def clear(self, fromIndex=0, toIndex=-1):
        '''Sets the bits from the specified fromIndex (inclusive) to the specified toIndex (exclusive) to false.'''
        return None
    def nextClearBit(self, fromIndex):
        '''Returns the index of the first bit that is set to false that occurs on or after the specified starting index.'''
        return 0
    def previousClearBit(self, fromIndex):
        '''Returns the index of the nearest bit that is set to false that occurs on or before the specified starting index.'''
        return None


    def length(self):
        '''Returns the "logical size" of this BitSet: the index of the highest set bit in the BitSet plus one.'''
        return 0
    def cardinality(self):
        '''Returns the number of bits set to true in this BitSet.'''
        return None
    def size(self):
        '''Returns the number of bits of space actually in use by this BitSet to represent bit values.'''
        return 0
    def isEmpty(self):
        '''Returns true if this BitSet contains no bits that are set to true.'''
        return False
    def clone(self):
        '''Cloning this BitSet produces a new BitSet that is equal to it.'''
        return None
    def hashCode(self):
        '''Returns the hash code value for this bit set.'''
        return None
    def equals(self, obj):
        '''Compares this object against the specified object.'''
        return False
    def intersects(self, bset):
        '''Returns true if the specified BitSet has any bits set to true that are also set to true in this BitSet.'''
        return None

    def stream(self):
        '''Returns a stream of indices for which this BitSet contains a bit in the set state.'''
        return None
    def toByteArray(self):
        '''Returns a new byte array containing all the bits in this bit set.'''
        return None
    def toLongArray(self):
        '''Returns a new long array containing all the bits in this bit set.'''
        return None
    def toString(self):
        '''Returns a string representation of this bit set.'''
        return None

    def And(self, bset):
        '''Performs a logical AND of this target bit set with the argument bit set.'''
        return None
    def Or(self, bset):
        '''Performs a logical OR of this bit set with the bit set argument.'''
        return None
    def andNot(self, bset):
        ''' Clears all of the bits in this BitSet whose corresponding bit is set in the specified BitSet.'''
        return None
    def xor(self, bset):
        '''Performs a logical XOR of this bit set with the bit set argument.'''
        return None

import time

ISOTIMEFORMAT = '%Y-%m-%d %X'

cap = 4000000
size = 8

print('start BitSet test.')
print()
print('cap:', cap, '; size:', size, '; bites:', cap * size)
print()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start create BitSet.')
bs = BitSet(cap, size)
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end create BitSet.')
print()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start set.')
start = time.time()
for i in range(cap * size):
	bs.setOne(i)
	#bit = bs.getOne(i)
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end set.')
print('totail time: ', end - start, ' seconds.')
print((cap * size) / (end * 1000 - start * 1000) , ' times set per ms.')

print()

print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'start get.')
start = time.time()
for i in range(cap * size):
	#bs.setOne(i)
	bit = bs.getOne(i)
end = time.time()
print(time.strftime( ISOTIMEFORMAT, time.localtime()), 'end get.')
print('totail time: ', end - start, ' seconds.')
print((cap * size) / (end * 1000 - start * 1000) , ' times get per ms.')
