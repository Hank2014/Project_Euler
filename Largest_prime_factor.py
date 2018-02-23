import sys
import math

def Big_prime_factor(a,b,start):
  global lim 
  if a % 2==0:
    b = 2 
    while a % 2==0:
      a /= 2
    lim = int( math.sqrt(long(a)))
  for x in range (start, lim, 2):
    if a % x==0 :
      b = x
      while a % x==0:
        a /= x
      lim = int(math.sqrt(long(a)))
      return Big_prime_factor(a,b,b)
  if a != 1:
    return str(a)
  return str(b)

lim = int (math.sqrt(long(sys.argv[1])))
print("Answer is "+Big_prime_factor(long(sys.argv[1]),1,3) +"\n")
