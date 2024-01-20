# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 18:57:10 2024

@author: GeetArjun
"""

l=[] #empty list
print(l) 

l1=[10,20,30,40]
print(l1)

l3="dypimca" #string to list
print(list(l3))

l4="welcome to all".split()  #list split
print(l4)

l5=[12,13,"dypimca","hello"] #slicing
print(l5[3][1])

#Function
l6=[12,15,15,17,"dypimca"] 
l6.append(16)     #append
print(l6)

l6.insert(2,10)  #insert
print(l6)

print(l6.pop())  #pop
print(l6.remove(15))  #remove

print(len(l6))  #length

print(l6.count(15)) #count


