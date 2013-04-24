
triplets = ((a, b, 1000-a-b) for a in xrange(1,999) for b in xrange(a+1, 999))
print (a*b*c for (a, b, c,) in triplets if a**2 + b**2 == c**2).next()
