from math import sqrt

def even(num):
  return num % 2 == 0

def odd(num):
  return num % 2 == 1

def fib(num):
  if num < 0:
    raise ValueError

  if num in fib._values:
      return fib._values[num]
  else:
      fibval = fib(num - 1) + fib(num - 2)
      fib._values[num] = fibval
      return fibval
fib._values = {0: 0, 1: 1}

def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

def lcm(a, b):
  return (a * b) // gcd(a, b)

def prime_factors(num, start=2):
  '''Return all prime factors (ordered) of num in a list'''
  candidates = xrange(start, int(sqrt(num)) + 1)
  factor = next((x for x in candidates if (num % x == 0)), None)
  return ([factor] + prime_factors(num / factor, factor) if factor else [num])
