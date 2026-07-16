# defining a function

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n* fact(n-1)

def print_fact(n):
    result=fact(n)
    print(f"the factorail of {n} is {result}")

print_fact(5)

import math_module as M

num1 = 12
num2 = 3
print("Addition of  numbers is ", M.add(num1,num2))
print("Subtraction  of  numbers is ", M.sub(num1,num2))
print("Division of  numbers is ", M.div(num1,num2))

st="Watermelon"
print("".join(reversed(st)))
print(st[::-1])
