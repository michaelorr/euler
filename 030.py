#! /usr/bin/python
from itertools import count

powers = {'0':0,
          '1':1, 
          '2':32, 
          '3':243, 
          '4':1024, 
          '5':3125,
          '6':7776,
          '7':16807,
          '8':32768,
          '9':59049}

valids = []

for i in count(2):
  if i >354295: break

  total = 0

  for j in str(i):
    total += powers[j]
  if i == total:
    print "found a valid: %d" % i
    valids.append(i)


print sum(valids)
