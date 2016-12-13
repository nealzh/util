#!/usr/bin/python
# -*- coding: utf-8 -*-

from CountingSet import CountingSet
import math
import mmh3

class CountingBloomFilter(object):

    mask32 = 0xffffffff
    mask64 = 0xffffffffffffffff
    mask128 = 0xffffffffffffffffffffffffffffffff
    
    seeds = [2, 3, 5, 7, 11, 
            13, 17, 19, 23, 29, 
            31, 37, 41, 43, 47, 
            53, 59, 61, 67, 71, 
            73, 79, 83, 89, 97, 
            101, 103, 107, 109, 113, 
            127, 131, 137, 139, 149, 
            151, 157, 163, 167, 173, 
            179, 181, 191, 193, 197, 
            199, 211, 223, 227, 229, 
            233, 239, 241, 251, 257, 
            263, 269, 271, 277, 281, 
            283, 293, 307, 311, 313, 
            317, 331, 337, 347, 349, 
            353, 359, 367, 373, 379, 
            383, 389, 397, 401, 409, 
            419, 421, 431, 433, 439, 
            443, 449, 457, 461, 463, 
            467, 479, 487, 491, 499, 
            503, 509, 521, 523, 541, 
            547, 557, 563, 569, 571, 
            577, 587, 593, 599, 601, 
            607, 613, 617, 619, 631, 
            641, 643, 647, 653, 659, 
            661, 673, 677, 683, 691]
    
    def __init__(self, n, fpr=0.00001, countingLength=16):
        
        m = -1 * math.log(fpr, math.e) * n / math.pow(math.log(2, math.e), 2)
        k = (m / n) * math.log(2, math.e)
        
        self.n = int(math.ceil(n))
        self.fpr = fpr
        self.m = int(math.ceil(m))
        self.k = int(k)

        self.bsUnitSize = countingLength
        self.bsCap = self.m 

        self.countingSet = CountingSet(self.bsCap, self.bsUnitSize)
        self.countingSetLength = self.countingSet.length
        
    def append(self, s):
        self.countingSet.addList(self.hashs(s, self.k))

    def exists(self, s):
        bites = self.countingSet.getList(self.hashs(s, self.k))
        return min(bites)
    
    def remove(self, s):
        self.countingSet.setList(self.hashs(s, self.k), 0)
        
    def clear(self):
        self.countingSet.clear()

    def hashs(self, s, k):
        countingSetLength = self.countingSetLength
        #mask = self.mask32
        mask = self.mask128
        seeds = self.seeds
        
        hashs = []
        for i in range(k):
            #print(mmh3.hash64(s, seeds[i]))
            #hashs.append((mmh3.hash(s, seeds[i]) & mask) % countingSetLength)
            hashs.append((mmh3.hash128(s, seeds[i]) & mask) % countingSetLength)
        return hashs

    def hashs2(self, s, k):

        countingSetLength = self.countingSetLength
        mask = self.mask32
        
        hashs = []
        hash1 = mmh3.hash64(s, 0)
        hash2 = mmh3.hash64(s, hash1)

        for i in k:
            hashs.append(((hash1 + i * hash2) % countingSetLength) & mask)
        return hashs
