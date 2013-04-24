from util import triangle_number, first, ilen, divisors
from itertools import count

triangles = (triangle_number(n) for n in count(1))
print first(t for t in triangles if ilen(divisors(t)) > 500)
