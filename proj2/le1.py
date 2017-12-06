# lab exercise 1

from sympy import *
from sympy import Poly

x = symbols('x')
print('part1')
p1 = Poly(x**23+x**5+1,modulus=2)
pprint(p1.is_irreducible)
pprint(p1.is_primitive)

print('part2')
p2 = Poly(x**23+x**6+1,modulus=2)
pprint(p2.is_irreducible)
print(factor(x**23+x**6+1,modulus=2))

print('part3')
p3= Poly(x**18+x**3+1,modulus=2)
pprint(p3.is_irreducible)
pprint(p3.is_primitive)
 
print('part4')
p4 = Poly(x**8+x**6+1,modulus=7) 
pprint(p4.is_irreducible)
print(factor(x**8+x**6+1,modulus=7))

