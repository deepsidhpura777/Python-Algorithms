# -*- coding: utf-8 -*-
"""
Created on Wed May 04 10:17:43 2016

@author: Deep Sidhpura
"""

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashFunction(self,key,size):
        return key%size       
        
    def rehashFunction(self,oldhash,size):
        return (oldhash+1)%size
        
    def add(self,key,value):
        position = self.hashFunction(key,self.size)
        if self.slots[position] == None:
            self.slots[position] = key
            self.data[position] = value
            
        else:
            if self.slots[position] == key:
                self.data[position] = value
                
            else:
                reposition = self.rehashFunction(position,self.size)
                while self.slots[reposition] != None:
                    reposition = self.rehashFunction(reposition,self.size)
                    
                self.slots[reposition] = key
                self.data[reposition] = value
                
                
    def get(self,key):
        start = self.hashFunction(key,self.size)
        temp = start
        found = False
        stop = False
        value = None
        while self.slots[temp] != None and not found and not stop:
            if self.slots[temp] == key:
                value = self.data[temp]
                found = True
            else:
                temp = self.rehashFunction(temp,self.size)   ### Stop if the rehash function produces the same hash as started
                if temp == start:
                    stop = True
        return value
        
h = HashTable()
h.add(54,"Deep")
h.add(26,"Nidhi")
h.add(93,"Daksha")
h.add(17,"Jatin")
h.add(77,"Goku")
h.add(31,"Naruto")
h.add(44,"Sakura")
h.add(55,"Sasuke")
h.add(20,"Vegeta")
h.add(88,"Ino")
h.add(25,"Kristen")

h.data
                
                
        
        