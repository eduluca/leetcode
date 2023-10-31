import numpy as np
import matplotlib.pyplot as plt

# Data points
X = np.array([[1, 0], [4, 2], [0, -1], [-1, -1], [-2, 1]])
t = np.array([1, 1, -1, -1, -1])

# Initial weights and intercept
w = np.array([4, 1])
w_0 = 2

# Scatter plot of data points
plt.scatter(X[t == 1][:, 0], X[t == 1][:, 1], label='Class 1', marker='o')
plt.scatter(X[t == -1][:, 0], X[t == -1][:, 1], label='Class -1', marker='x')

# Decision boundary
x_line = np.linspace(-2.5, 4.5, 100)
y_line = -(w[0] / w[1]) * x_line - (w_0 / w[1])
plt.plot(x_line, y_line, label='Decision Boundary', color='red')

plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()
plt.title("Perceptron Classifier Decision Boundary")
plt.grid(True)
plt.show()