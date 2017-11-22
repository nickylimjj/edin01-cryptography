# lab exercise 1

from sympy import *
from sympy import Poly

x = symbols('x')
print('part1')
print(latex(factor(x**23+x**5+1,modulus=2)))

print('part2')
print(latex(factor(x**23+x**6+1,modulus=2)))

print('part3')
print(latex(factor(x**18+x**3+1,modulus=2)))
 
print('part4')
print(latex(factor(x**8+x**6+1,modulus=7)))

