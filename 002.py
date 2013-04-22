from util import fib, even

from itertools import count, takewhile

def fib_gen():
  for i in count():
      yield fib(i)

print sum(n for n in takewhile(lambda x: x < 4000000, fib_gen()) if even(n))
