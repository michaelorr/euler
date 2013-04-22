lower_bound = 100
upper_bound = 1000

biggest = 0

for i in xrange(lower_bound, upper_bound):
  for j in xrange(lower_bound, upper_bound):
    product = str(i * j)
    if product == ''.join(reversed(product)):
      biggest = max(biggest, int(product))
        
print biggest
