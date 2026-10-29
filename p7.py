# AIM: Implement Neural Network using Backpropagation

import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Training data
X = np.array([
    [0, 0, 1],
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 1]
])

Y = np.array([[0, 1, 1, 0]]).T

# Initialize weights randomly
np.random.seed(1)
weights = 2 * np.random.random((3, 1)) - 1

# Train the neural network
for i in range(15000):
    output = sigmoid(np.dot(X, weights))
    error = Y - output
    weights += np.dot(X.T, error * output * (1 - output))

# Display final output
print("Output after training:")
print(sigmoid(np.dot(X, weights)))