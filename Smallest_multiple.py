#we first do integer factorization and calculate of all numbers from 1 to 10, then observe
#that for example, math.floor(log2(10))=3, so this means , for the base 2, we only need 3 
#of them to represent all the natural numbers smaller than 10
 
import math #log


def smallest_multiple (num):
  mult = 1;
  Prime = [2,3,5,7,11,13,17,19]
 
  for x in Prime:
    if(x>num):
      break
    mult *= x**int(math.log(num,x))
    print(str(x)+" = "+ str(mult)+"\n")

smallest_multiple(20)
