from collections import Counter

distances = Counter()
distances[1] = 1

def even(n):
  return n % 2 == 0

def if_even(n):
  return n / 2

def if_odd(n):
  return n*3 + 1

def collatz_distance(n):
  if distances[n] == 0:
    next_collatz = if_even if even(n) else if_odd
    distances[n] = collatz_distance(next_collatz(n)) + 1

  return distances[n]


for n in xrange(1,1000000):
  collatz_distance(n)

print distances.most_common(1)
