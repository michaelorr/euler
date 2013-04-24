from operator import mul

with open('./data/008/num.txt') as f:
    data = f.read()

largest = 0

for index in xrange(len(data[:-5])):
  val = reduce(mul, map(int, data[index:index+5]))
  largest = max(largest, val)

print largest