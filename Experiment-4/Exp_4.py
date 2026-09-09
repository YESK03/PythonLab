# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 08:05:40 2026

@author: user
"""

integers = [6, 7, 8, 9, 10, 11, 12, 13 ,14 ,15,6,61]

print("Original List:", integers)


print("Length of list", len(integers))

integers.append(16)
print("After Append 16 ", integers)

integers.insert(5, 40)
print("After inserting", integers)

integers.remove(10)
print("After removing", integers)

integers.pop(5)
print("After Poping",integers)

print("Count",integers.count(6))

print("Index ",integers.index(15))

#START
print(integers[0:5])
#REVERSE
print(integers[-1])

x = integers.copy()
print(x)

integers.extend(x)
print("Extend", integers)









