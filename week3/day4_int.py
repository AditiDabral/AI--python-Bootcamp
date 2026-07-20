# integral : I am not good in this topic ,
# application ML : Cost functions , probabiity distribution 

import sympy as sp

x = sp.Symbol('x')
f = x**2
definite_integral = sp.integrate(f, (x, 0, 2)) # integrate function f from 0 to 2

indefinite_integral = sp.integrate(f,x)

print("Definite Integral: ",definite_integral)
print("Indefinte Integral:", indefinite_integral)
