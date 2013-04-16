from util import fib, even

from itertools import count

def fib_gen():
  for i in count():
      res = fib(i)
      if res > fib_gen._sentinel:
        raise StopIteration
      yield res
fib_gen._sentinel = 4000000


print sum(n for n in fib_gen() if even(n))
