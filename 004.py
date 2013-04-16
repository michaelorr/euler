lower_bound = 100
upper_bound = 1000

biggest = 0

for i in xrange(lower_bound, upper_bound):
  for j in xrange(lower_bound, upper_bound):
    product = i * j
    product_str = str(product)
    if product_str == ''.join(reversed(product_str)):
      biggest = max(biggest, product)
        
print biggest
