#! /usr/bin/python
from itertools import count

facts = {'0':1,
         '1':1,
         '2':2,
         '3':6,
         '4':24,
         '5':120,
         '6':720,
         '7':5040,
         '8':40320,
         '9':362880}

running_total = 0

for i in count(3):
  if i > 2540161:
    break

  total = 0

  for t_place in str(i):
    total += facts[t_place]
  
  if total == i:
    running_total += i

print running_total
      
