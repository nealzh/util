#!/usr/bin/python
# -*- coding: utf-8 -*-

import array

class FastBitSet(object):
    
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
        
        self.fullMask = 18446744073709551615 >> (64 - unitSize)
        
        pool = array.array(self.unitType, [0])
        
        for i in range(capacity - 1):
            pool.append(0)
        
        self.pool = pool

    def get(self, fromIndex, length=1):
        
        '''Returns a new BitSet composed of bits from this BitSet from fromIndex (inclusive) to toIndex (exclusive).'''

        if(length == 1):
            return getOne(fromIndex)
        
        if((fromIndex) + length > self.length):
            raise Exception('BitSet out of index.')
        
        bucketIndex, unitIndex = divmod(fromIndex, self.unitSize)
        endBucketIndex, endUnitIndex = divmod(fromIndex + length - 1, self.unitSize)
        fullMask = self.fullMask
        bits = []
        
        if(bucketIndex == endBucketIndex):
            
            mask = (fullMask >> (self.unitSize - length)) <<  unitIndex
            bits.append((self.pool[bucketIndex] & mask) >> unitIndex)
            
        else:
            for i in range(bucketIndex, endBucketIndex + 1):
                if(i == bucketIndex):
                    mask = (fullMask >> unitIndex) <<  unitIndex
                    bits.append((self.pool[i] & mask) >> unitIndex)
                    
                elif(i == endBucketIndex):
                    mask = fullMask >> (self.unitSize - endUnitIndex - 1)
                    bits.append(self.pool[i] & mask)
                    
                else:
                    bits.append(self.pool[i] & fullMask)
        return bits
        
    def getList(self, indexes):

        '''Returns the value of the bit with the specified indexes.'''

        bits = []
        
        for index in indexes:
            
            if(index >= self.length):
                raise Exception('BitSet out of index.')
            
            bucketIndex, unitIndex = divmod(index, self.unitSize)
            
            mask = 1 << unitIndex
        
            bits.append((self.pool[bucketIndex] & mask) >> unitIndex)
            
        return bits
    
    def getOne(self, index):
        
        '''Returns the value of the bit with the specified index.'''
        
        if(index >= self.length):
            raise Exception('BitSet out of index.')
        
        bucketIndex, unitIndex = divmod(index, self.unitSize)
        mask = 1 << unitIndex
        
        return (self.pool[bucketIndex] & mask) >> unitIndex

    def set(self, fromIndex, length=1, value=True):
        
        '''Sets the bits from the specified fromIndex (inclusive) to the specified toIndex (exclusive) to the specified value.'''

        if((fromIndex) + length > self.length):
            raise Exception('BitSet out of index.')

        if(length == 1):
            return setOne(fromIndex, value)
        
        bucketIndex, unitIndex = divmod(fromIndex, self.unitSize)
        endBucketIndex, endUnitIndex = divmod(fromIndex + length - 1, self.unitSize)

        fullMask = self.fullMask

        #change in same bucket
        if(bucketIndex == endBucketIndex):
            
            mask = (fullMask >> (self.unitSize - length)) <<  unitIndex

            #set 1
            if(value):
                self.pool[bucketIndex] = self.pool[bucketIndex] | mask
                
            #set 0
            else:
                self.pool[bucketIndex] = self.pool[bucketIndex] & (mask ^ fullMask)

        #change in diffent bucket
        else:
            #set 1
            if(value):
                #change between bucketIndex and endBucketIndex
                for i in range(bucketIndex, endBucketIndex + 1):

                    #first bucket
                    if(i == bucketIndex):
                        
                        mask = (self.fullMask >> unitIndex) <<  unitIndex
                        self.pool[i] = self.pool[i] | mask

                    #end bucket
                    elif(i == endBucketIndex):
                        
                        mask = self.fullMask >> (self.unitSize - endUnitIndex - 1)
                        self.pool[i] = self.pool[i] | mask

                    #middle of the start and end
                    else:
                        
                        self.pool[i] = fullMask

            #set 0
            else:
                #change between bucketIndex and endBucketIndex
                for i in range(bucketIndex, endBucketIndex + 1):

                    #first bucket
                    if(i == bucketIndex):
                        
                        mask = ((self.fullMask >> unitIndex) <<  unitIndex) ^ fullMask
                        self.pool[i] = self.pool[i] & mask

                    #end bucket
                    elif(i == endBucketIndex):
                        
                        mask = (self.fullMask >> (self.unitSize - endUnitIndex - 1)) ^ fullMask
                        self.pool[i] = self.pool[i] & mask

                    #middle of the start and end
                    else:
                        
                        self.pool[i] = 0


    def setList(self, indexes, value=True):
        
        '''Sets the bit at the specified indexes to the specified value.'''

        if(value):
            for index in indexes:
                if(index >= self.length):
                    raise Exception('BitSet out of index.')
                bucketIndex, unitIndex = divmod(index, self.unitSize)
                mask = 1 << unitIndex
                self.pool[bucketIndex] = self.pool[bucketIndex] | mask
            
        else:
            for index in indexes:
                if(index >= self.length):
                    raise Exception('BitSet out of index.')
                bucketIndex, unitIndex = divmod(index, self.unitSize)
                mask = 1 << unitIndex
                self.pool[bucketIndex] = self.pool[bucketIndex] & (mask ^ self.fullMask)

    def setOne(self, index, value=True):
        
        '''Sets the bit at the specified index to the specified value.'''
        
        if(index >= self.length):
            raise Exception('BitSet out of index.')
        
        bucketIndex, unitIndex = divmod(index, self.unitSize)

        mask = 1 << unitIndex

        if(value):
            self.pool[bucketIndex] = self.pool[bucketIndex] | mask
        else:
            self.pool[bucketIndex] = self.pool[bucketIndex] & (mask ^ self.fullMask)
        
    def nextSetBit(self, fromIndex, value=True):
        '''Returns the index of the first bit that is set to true that occurs on or after the specified starting index.'''
        self.set(fromIndex, self.length - fromIndex, value)
        
    def previousSetBit(self, fromIndex, value=True):
        '''Returns the index of the nearest bit that is set to true that occurs on or before the specified starting index.'''
        self.set(0, fromIndex - 1, value)
    
    def flip(self, fromIndex, length=1):
        
        '''Sets each bit from the specified fromIndex (inclusive) to the specified toIndex (exclusive) to the complement of its current value.'''
        
        if((fromIndex) + length > self.length):
            raise Exception('BitSet out of index.')

        if(length == 1):
            return flipOne(fromIndex)
        
        bucketIndex, unitIndex = divmod(fromIndex, self.unitSize)
        endBucketIndex, endUnitIndex = divmod(fromIndex + length - 1, self.unitSize)

        fullMask = self.fullMask
        
        if(bucketIndex == endBucketIndex):
            
            mask = (fullMask >> (self.unitSize - length)) <<  unitIndex
            self.pool[bucketIndex] = self.pool[bucketIndex] ^ mask
            
        else:
            for i in range(bucketIndex, endBucketIndex + 1):
                if(i == bucketIndex):
                    mask = (fullMask >> unitIndex) <<  unitIndex
                    self.pool[bucketIndex] = self.pool[bucketIndex] ^ mask
                elif(i == endBucketIndex):
                    mask = fullMask >> (self.unitSize - endUnitIndex - 1)
                    self.pool[bucketIndex] = self.pool[bucketIndex] ^ mask
                else:
                    self.pool[bucketIndex] = self.pool[bucketIndex] ^ fullMask
    
    def flipOne(self, index):
        
        '''Sets the bit at the specified index to the complement of its current value.'''
        
        if(index >= self.length):
            raise Exception('BitSet out of index.')
        
        bucketIndex, unitIndex = divmod(index, self.unitSize)

        mask = 1 << unitIndex

        self.pool[bucketIndex] = self.pool[bucketIndex] ^ mask

    def clear(self):
        
        '''Sets the bits from the specified fromIndex (inclusive) to the specified toIndex (exclusive) to false.'''

        pool = self.pool
        
        for i in range(self.capacity):
            pool[i] = 0

    
    def nextClearBit(self, fromIndex):
        
        '''Returns the index of the first bit that is set to false that occurs on or after the specified starting index.'''
        
        bucketIndex, unitIndex = divmod(index, self.unitSize)

        if(unitIndex != (self.unitSize - 1)):
            mask = fullMask >> (self.unitSize - unitIndex - 1)
            self.pool[bucketIndex] = self.pool[bucketIndex] & mask

        bucketIndex = bucketIndex + 1

        for i in range(bucketIndex, self.cap):
            self.pool[i] = 0
        
    def previousClearBit(self, fromIndex):
        
        '''Returns the index of the nearest bit that is set to false that occurs on or before the specified starting index.'''

        bucketIndex, unitIndex = divmod(index, self.unitSize)

        if(unitIndex != 0):
            mask = (fullMask >> unitIndex) << unitIndex
            self.pool[bucketIndex] = self.pool[bucketIndex] & mask

        bucketIndex = bucketIndex - 1

        for i in range(0, bucketIndex):
            self.pool[i] = 0

    def length(self):
        '''Returns the "logical size" of this BitSet: the index of the highest set bit in the BitSet plus one.'''
        return self.length
    def cardinality(self):
        '''Returns the number of bits set to true in this BitSet.'''
        return None
    def size(self):
        '''Returns the number of bits of space actually in use by this BitSet to represent bit values.'''
        return 0
    
    def isEmpty(self):
        
        '''Returns true if this BitSet contains no bits that are set to true.'''

        b = False

        for i in range(self.capacity):
            b = b | (self.pool[i] > 0)
        
        return b
    
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
