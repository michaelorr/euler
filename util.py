def even(num):
  '''
  shorthand
  '''
  return num % 2 == 0

def odd(num):
  '''
  shorthand
  '''
  return num % 2 == 1

def fib(num):
  '''
  Calculates Fibonacci numbers while remembering previous results
  '''
  if num < 0:
    raise ValueError

  if num in fib._values:
      return fib._values[num]
  else:
      fibval = fib(num - 1) + fib(num - 2)
      fib._values[num] = fibval
      return fibval
fib._values = {0: 0, 1: 1}