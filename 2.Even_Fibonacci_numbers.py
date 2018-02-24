from math import sqrt
def even_fibonacci_numbers(x):
  sum = 0
  for i in xrange(0,300):
    if i%3 == 0:
      if F(i)<=x:
        print(F(i))
        sum += F(i)
      else:
        break
  print(sum)

def F(n):
  return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))



even_fibonacci_numbers(4000000)
