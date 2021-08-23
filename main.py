# -*- coding: utf-8 -*-
"""Utilities for writing code that runs on Python 2 and 3"""

count = 1
mass = list(range(1,100,4))
print(mass, mass.__class__)
list1 = list('asdfghjkl')
#while True:
    #print(count)
    #count += 1
#print(count)

for i in list1:
    print (i)

string1 = '    werqwe  123 12 123 1123  123 12  356  34 t4 3 3 3 3   3r42'
l1 = string1.split(' ')
string2 = ''
for i in l1:
    if i != '':
        string2 += i + ' '
print(string2)