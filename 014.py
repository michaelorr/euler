
def if_odd(n):
  return 3 * n + 1

def if_even(n):
  return n / 2

def calculate_collatz(n):
  # print "calculating the collatz of %d" % n
  collatz = [n]
  if n != 1:
    next = if_even(n) if n % 2 == 0 else if_odd(n)
    collatz.extend(calculate_collatz(next))
  return collatz


longest = -1
for i in xrange(1, 1000000):
  i_length = len(calculate_collatz(i))
  if i_length > longest:
      longest = i_length

print longest