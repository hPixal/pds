import numpy as np
from scipy.signal import lfilter
import matplotlib.pyplot as plt

def convolution(x, h):
    res = np.zeros(len(x) + len(h) - 1)
    for n in range(len(res)):
        for k in range(len(h)):
            if n - k >= 0 and n - k < len(x):
                res[n] += x[n - k] * h[k]
    return res
    
# Test the convolution function
# Define two signals
x = np.array([1, 1, 1, 1, 1])
h = np.array([0.2, 0.6, 0.2])

# Perform convolution
y = convolution(x, h)

# Perform convolution using numpy's conv function
y_conv = np.convolve(x, h, mode='full')

# Perform convolution using scipy's lfilter function
y_filter = lfilter(h, [1.0], x)

# Plot the signals
plt.figure(figsize=(12, 8))

# Input signal
plt.subplot(4, 1, 1)
plt.stem(x)
plt.title("Input Signal x[n]")
plt.grid()

# Impulse response
plt.subplot(4, 1, 2)
plt.stem(h)
plt.title("Impulse Response h[n]")
plt.grid()

# Convolved signal (custom function)
plt.subplot(4, 1, 3)
plt.stem(y)
plt.title("Convolved Signal y[n] (Custom Function)")
plt.grid()

# Comparison with numpy's conv and scipy's filter
plt.subplot(4, 1, 4)
plt.stem(y_conv, markerfmt='C1o', linefmt='C1-', basefmt='C1-', label='np.convolve')
plt.stem(y_filter, markerfmt='C2x', linefmt='C2--', basefmt='C2--', label='scipy.lfilter')
plt.title("Comparison with np.convolve and scipy.lfilter")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()