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

list2 = ['1','2','30']
list2.insert(2,'3')
print(list2)
list2.insert(20,'323')
list2[1:2] = ['sdfs', 'sdfss']
number_things  = (number for number in range(1,6))
print(type(number_things), number_things)
set1 = set('122121235455123111')
print(set1)