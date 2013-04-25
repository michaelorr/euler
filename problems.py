#!python
import data

from util import *

from itertools import takewhile
from operator import mul

def problem1():
  return sum(n for n in xrange(1000) if n % 3 == 0 or n % 5 == 0)
  
def problem2():
  return sum(j for j in takewhile(lambda x: x < 4000000, fibs()) if even(j))

def problem3():
  return prime_factors(600851475143)[-1]

def problem4():
  return max(i*j for i in xrange(100, 1000) for j in xrange(i, 1000) if is_palindrome(i*j))

def problem5():
  return reduce(lcm, xrange(1, 20))

def problem6():
  return pow(sum(xrange(1, 101)), 2) - sum(pow(x, 2) for x in xrange(1, 101))

def problem7():
  return index(10000, primes())

def problem8():
  digits = ''.join(data.problem8.strip().splitlines())
  return max(reduce(mul,map(int, list(digits[i:i+5]))) for i in xrange(len(digits[:-4])))

def problem9():
  triplets = ((a, b, 1000-a-b) for a in xrange(1,999) for b in xrange(a+1, 999))
  return (a*b*c for (a, b, c,) in triplets if a**2 + b**2 == c**2).next()

def problem10():
  return sum(takewhile(lambda x: x < 2000000, primes()))

def problem11():
  pass

def problem12():
  return None
  # triangles = (triangle_number(n) for n in count(1))
  # return first(t for t in triangles if ilen(divisors(t)) > 500)
  
