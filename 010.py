from itertools import takewhile

from util import primes

limit = 2000000

print sum(takewhile(lambda x: x < limit, primes()))
