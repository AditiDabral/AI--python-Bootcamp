import numpy as np

# The model starts by guessing.
# It checks how wrong the guess is.
# It figures out whether it should increase or decrease its parameters.
# It moves only a little (learning rate).
# It repeats this process until the error is minimized.
# #Implement Gradient for Linear Regression

# Define the gradient descent function
def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)
    for _ in range(iterations):
        predictions = np.dot(X, theta)
        errors = predictions -y
        gradient = (1/m) * np.dot(X.T, errors)
        theta -= learning_rate * gradient
    return theta 

#sample data
X = np.array([[1,1],[1,2],[1,3]])
y = np.array([2,2.5, 3.5])
theta = np.array([0.1, 0.2])
learning_rate = 0.1
iteration = 1000

#Perform gradient descent
optimized_theta = gradient_descent(X, y, theta, learning_rate , iteration )
print("Optimized Parameters:",optimized_theta)

# debug
# Start with some random values of theta.
# theta = [0.1, 0.2]

# Equation: y = θ₀ + θ₁x

# y = 0.1 + 0.2x

# Make Predictions

# x = 1
# Prediction: 0.1 + (0.2 * 1) = 0.3 
# x = 2 
# Prediction: 0.1 + (0.2 * 2) = 0.5

# x = 3 
# Prediction: 0.1 + (0.2 × 3) = 0.7 

# Predictions: [0.3, 0.5, 0.7]

# Calculate Errors :

# Actual Values:

# [2, 2.5, 3.5]


# Predicted Values:

# [0.3, 0.5, 0.7]

# Errors:  0.3 - 2 = -1.7 , 0.5 - 2.5 = -2 , 0.7 - 3.5 = -2.8
# Errors = [-1.7, -2, -2.8]

# The negative sign tells us that our predictions are too small.

# So, we need to increase our theta values.

# Question: How much should we increase theta?

# Gradient answers this question. Large Error --> Large Change ,  Small Error --> Small Change

# The computer calculates:

# Gradient = (1/m) * (Xᵀ * Errors)
# Gradient = [-2.16, -4.7]

# Update Theta Values
# Formula:

# New Theta = Old Theta − (Learning Rate * Gradient)

# Suppose:
# Learning Rate = 0.1 

# Old Theta: [0.1, 0.2]

# Gradient: [-2.16, -4.7]

# Then, New Theta becomes approximately: [0.316, 0.67] 

# REPEAT THE PROCESS Until it become minimum error 