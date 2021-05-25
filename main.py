#Count prime number from given range

import sympy
limit = int(input("Range start from:"))
limit1 = int(input("Range ends at:"))
i = list(sympy.primerange(limit, limit1+1))
r = len(i)
print("Total Prime numbers are: ",r)
print("List of prime numbers:",i)