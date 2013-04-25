#!python
from itertools import count, islice, ifilter, takewhile, groupby, product

from collections import Counter

from math import sqrt

def even(num):
  '''tests evenness'''
  return num % 2 == 0

def odd(num):
  '''tests oddness'''
  return not even(num)

def fib(num):
  '''returns fib(num)'''
  if num < 0:
    raise ValueError

  if num in fib._values:
      return fib._values[num]
  else:
      fibval = fib(num - 1) + fib(num - 2)
      fib._values[num] = fibval
      return fibval
fib._values = {0: 0, 1: 1}

def fibs():
  '''returns a generator of sequential fibs starting with fib(1)'''
  return (fib(i) for i in count()) 

def gcd(a, b):
  '''returns the greatest common denominator of a and b'''
  while b:
    a, b = b, a % b
  return a

def lcm(a, b):
  '''returns the least common multiple of a and b'''
  return (a * b) // gcd(a, b)

def prime_factors(num, start=2):
  '''Return all prime factors (ordered) of num in a list'''
  candidates = xrange(start, int(sqrt(num)) + 1)
  factor = next((x for x in candidates if (num % x == 0)), None)
  return ([factor] + prime_factors(num / factor, factor) if factor else [num])

def primes(start=2):
  '''returns a generator of prime numbers'''
  return ifilter(is_prime, count(start))

def is_prime(n):
  '''tests primality of n'''
  if n < 3 or n % 2 == 0:
    return (n == 2)
  elif any((n % x == 0) for x in xrange(3, int(sqrt(n)) + 1, 2)):
    return False
  return True

def index(n, iterable):
  'Returns the nth item'
  return islice(iterable, n, n+1).next()

def eratosthenes(n):
  '''using the sieve of eratosthenes, generate all primes less than n'''
  multiples = set()
  for i in xrange(2, n+1):
    if i not in multiples:
      yield i
      multiples.update(xrange(i**2, n+1, i))

def triangle_number(num):
  '''returns sum of 1->num'''
  return sum(xrange(num+1))

def first(iterator):
  '''returns the first item of an iterator'''
  return iterator.next()

def ilen(iterator):
  '''Returns the length of an iterator. Will not return for infinite generators'''
  return sum(1 for _ in iterator)

def is_palindrome(num):
  '''Tests the palindromicity of a number'''
  return num == int(''.join(reversed(str(num))))

def factorize(num):
  """Factorize a number returning occurrences of its prime factors"""
  return ((factor, ilen(fs)) for (factor, fs) in groupby(prime_factors(num)))

def divisors(n):
  '''Returns all divisors of num: divisors(16) -> 1, 2, 4, 8, 16'''
  all_factors = [[f**p for p in range(fp+1)] for (f, fp) in factorize(n)]
  return (product(ns) for ns in product(*all_factors))


def collatz(n):
  return ((n/2) if even(n) else (n*3 + 1))

def collatz_length(n):
  return 1 + collatz_length(collatz(n)) if n>1 else 0
