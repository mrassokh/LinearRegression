#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12.0, 9.0)

# Preprocessing Input data
data = pd.read_csv('data.csv')
X = data.iloc[:, 0]
Y = data.iloc[:, 1]
x_norm = (X - np.mean(X)) / np.std(X)
y_norm = (Y - np.mean(Y)) / np.std(Y)
theta_0 = 0
theta_1 = 0


# Building the model

L = 0.01  # The learning Rate
epochs = 200  # The number of iterations to perform gradient descent

n = float(len(X)) # Number of elements in X
print ("Number of elements in data is ")
print (n)
# Performing Gradient Descent
for i in range(epochs):
	# Calculate prediction with current theta in normalize range
	Y_pred = theta_0 + theta_1 * x_norm
	# Calculate derivative of goal function by theta_1
	D_theta_1 = (1/n) * sum(x_norm * (Y_pred - y_norm))
	# Calculate derivative of goal function by theta_0
	D_theta_0 = (1/n) * sum(Y_pred - y_norm)
	theta_1 = theta_1 - L * D_theta_1  # Update theta_1
	theta_0 = theta_0 - L * D_theta_0  # Update theta_0

# Calculate prediction with final theta in normalize range
Y_pred = theta_0 + theta_1 * x_norm
# Calculate prediction with final theta in denormalize range
Y_pred_denorm = Y_pred * np.std(Y) + np.mean(Y)

# Calculate denormalized theta
theta_1 = (Y_pred_denorm[0] - Y_pred_denorm[1]) / (X[0] - X[1])
theta_0 = Y_pred_denorm[0] - theta_1 * X[0]
X_max = -1 * theta_0 / theta_1;

print ("After learning theta_0 is ")
print (theta_0)
print ("and theta_1 is ")
print (theta_1)

# Plot data
plt.scatter(X, Y)
plt.xlabel('Milleage')
plt.ylabel('Price')
plt.title('Predicted price vs. milleage')
plt.plot(X, Y_pred_denorm, color='red')
plt.show()

# Save theta
np.savetxt("theta.csv", (theta_0,theta_1,X_max));
