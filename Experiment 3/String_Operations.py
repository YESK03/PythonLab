# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 08:01:23 2026

@author: user
"""

s = "Hello python"

print("Original String:",s)

print("Length :",len(s))

print("Uppercase:",s.upper())

print("Lowercase:",s.lower())

print("Character at 6 index",s[6])

print("Position of Python:",s.find("Python"))

print("Replace:",s.replace("Python", "World"))

print(s)

print("Contains Python:","Python" in s)

print("Concatenation:", s + "Programming")

s2 = " Hello      World    "
print("Trim:", s2.strip())