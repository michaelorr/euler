from fractions import Fraction

from operator import mul

result = []

for i in range(10, 100):
    for j in range(10, 100):
        if j >= i:
          break
        if j % 10 == 0 and i % 10 == 0:
          continue

        str_i = str(i)
        str_j = str(j)

        if str_i[0] == str_j[0]:
          if int(str_i[1]) != 0:
            if Fraction(j, i) == Fraction(int(str_j[1]), int(str_i[1])):
              result.append(Fraction(j, i))
        if str_i[0] == str_j[1]:
          if int(str_i[1]) != 0:
            if Fraction(j, i) == Fraction(int(str_j[0]), int(str_i[1])):
              result.append(Fraction(j, i))
        if str_i[1] == str_j[0]:
          if int(str_i[0]) != 0:
            if Fraction(j, i) == Fraction(int(str_j[1]), int(str_i[0])):
              result.append(Fraction(j, i))
        if str_i[1] == str_j[1]:
          if int(str_i[0]) != 0:
            if Fraction(j, i) == Fraction(int(str_j[0]),int(str_i[0])):
              result.append(Fraction(j, i))

print reduce(mul, result)
