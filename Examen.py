###          Exercitiul 1          ###

import copy
print("Exercitiul 1")
a=[[1,2,3,4],[4,5,6,7]]

b=a

print('a and b before modify')

print(a)

print(b)

a[0][1]=10

print('a and b after modify. b was obtain as a copy of a')

print(a)
print(b)


b = copy.deepcopy(a)

a[0][1]=8
print('a si b cu deep copy')
print('a=',a)
print('b=',b)


#####          Exercitiul 2          #####


import functools

print(" ")
print("Exercitiul 2")

a = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]

e = list(filter(lambda t: t%2, map(lambda z: functools.reduce(lambda x, y: x + y, z), a)))

print(e)
