# Gradient Descent is an optimization algorithm used to find the minimum value of a function.
# It is commonly used in Machine Learning to minimize the loss or error of a model.
# It works by repeatedly updating the value of a variable in the direction opposite to the gradient


# x_{new}=x_{old}-\alpha f'(x)


# =====================================================
# CELL 1: IMPORT LIBRARY
# =====================================================

import matplotlib.pyplot as plt


# =====================================================
# CELL 2: DEFINE FUNCTION AND DERIVATIVE
# =====================================================

# Given function: y = (x + 3)^2 This is a quadratic function (parabola).

def function(x):
    return (x + 3) ** 2

# Derivative: dy/dx = 2(x + 3) The derivative tells us the slope of the function at a particular point.Positive derivative → Slope is upward. Negative derivative → Slope is downward. Zero derivative → Stationary point.

def derivative(x):
    return 2 * (x + 3)


# =====================================================
# CELL 3: INITIALIZE PARAMETERS
# =====================================================

x = 2               # Starting point
learning_rate = 0.1 #Controls the step size
iterations = 50 #	Maximum number of updates

x_values = []
y_values = []


# =====================================================
# CELL 4: APPLY GRADIENT DESCENT
# =====================================================

for i in range(iterations):

    # Calculate gradient
    grad = derivative(x)

    # Update x value
    x = x - learning_rate * grad

    # Store values
    x_values.append(x)
    y_values.append(function(x))


# =====================================================
# CELL 5: DISPLAY LOCAL MINIMUM
# =====================================================

print("Minimum value of x:", x)
print("Minimum value of y:", function(x))


# =====================================================
# CELL 6: PLOT GRAPH
# =====================================================

plt.plot(x_values, y_values, marker='o')

plt.title("Gradient Descent")
plt.xlabel("Iterations")
plt.ylabel("Function Value")

plt.grid()
plt.show()

