# derivative : Isi din ke liye to derivation padhi thi !!!!!!

import sympy as sp
x = sp.Symbol('x')
f = x**2
derivative = sp.diff(f)
print("derivative of (x)^2:\n",derivative)

# Partial derivative , gradient  : i know !!!
x1 , y1 = sp.symbols('x1 y1')
f1 = x1**2 + y1**2
grad_x =sp.diff(f1, x1)
grad_y = sp.diff(f1, y1)

print("Partial Derivatives:",grad_x , grad_y)
import sympy as sp

# Define the variable and function
x = sp.Symbol('x')
f = x**4 + 3*x**2 + 5

# Compute the second derivative (pass the variable and order)
f_second = sp.diff(f, x, 2)

print("Second derivative:", f_second)  # Output: 12*x**2 + 6


# gradient descent : iterative optimization algo used to minimize  func
#update parameters in the dir of the negative gradient to find mininum
#Find the values of the parameters that minimize the error (loss function).

# Suppose we're trying to fit a line:

# y=mx+b

# where:

# m = slope (weight)
# b = intercept (bias)

# Initially, the model guesses random values for m and b. Its predictions will usually be poor, producing a large error. Gradient Descent repeatedly updates these values to reduce that error.

# Gradient → tells us which direction increases the error.
# Gradient Descent → moves in the opposite direction to reduce the error.
# Learning Rate → determines how large each step should be.
# Loss Function → measures how wrong the model's predictions are.
# Optimization → the process of finding parameter values that minimize the loss.

# θnew ​= θold​− α∂θ / ∂J​

# θ = parameter (weight or bias)

# α = learning rate

# J = loss (cost) function

# ∂θ/∂J = gradient (the slope of the loss function)