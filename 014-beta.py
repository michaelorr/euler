longest = -1

def if_odd(n):
  return 3 * n + 1

def if_even(n):
  return n / 2


for n in xrange(2, 1000000):
  i_length = len(calculate_collatz(i))
  if i_length > longest:
      longest = i_length

print longest