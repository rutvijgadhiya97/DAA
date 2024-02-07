import numpy as np
import matplotlib.pyplot as plt
import time

def f(n):
    x = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            x = x + 1
    return x

n_values = np.arange(1, 1001,10)  # Values of n from 1 to 100
runtimes = np.zeros(len(n_values))

for idx, n in enumerate(n_values):
    start_time = time.time()  # Start timing
    result = f(n)  # Call the function
    end_time = time.time()  # Stop timing
    runtimes[idx] = end_time - start_time  # Record elapsed time

# Fit a polynomial curve (quadratic) to the data
coeffs = np.polyfit(n_values, runtimes, 2)
fit_curve = np.polyval(coeffs, n_values)

# Calculate upper and lower bounds based on the leading term of the fitted polynomial
upper_bound = 1.1 * np.polyval(coeffs, n_values)  # Adjust the constant factor as needed
lower_bound = 0.9 * np.polyval(coeffs, n_values)  # Adjust the constant factor as needed



# Plotting time vs n with different colors for curves
plt.figure()
plt.plot(n_values, runtimes, 'o-',linewidth=2, label='Actual Data')
plt.plot(n_values, fit_curve,  linewidth=2, label='Polynomial Fit')
plt.plot(n_values, upper_bound,  linewidth=2, label='Upper Bound (O(n^2))', color='green')
plt.plot(n_values, lower_bound,  linewidth=2, label='Lower Bound (Ω(n^2))', color='purple')
n_0=90
plt.scatter(n_0, np.polyval(coeffs, n_0), s=50, c='red', marker='s', label=r'n_0')
plt.text(n_0, np.polyval(coeffs, n_0), r'n_0', ha='right', va='bottom')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Runtime vs n')
plt.legend()

# Display the coefficients of the fitted polynomial (for reference)
print("Coefficients of the fitted polynomial:", coeffs)

plt.show()
