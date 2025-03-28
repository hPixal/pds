import numpy as np
import matplotlib.pyplot as plt

def senoidal(f_m, f_s, t_i, t_f, amp, alpha):
    x = np.arange(t_i, t_f, f_m)
    y = amp * np.sin(2 * np.pi * f_s * x + alpha)
    return x, y

def quantizer(x,h=0.5,n=8):
    rtn = []
    for x_0 in x :
        if x_0 < 0 : 
            rtn.append(0)
        if 0 <= x_0 and x_0 < (n-1)*h:
            rtn.append(h*np.round(x_0/h))
        if x_0 >= (n-1)/h :
            rtn.append((n-1)*h)
    return rtn

def power(s):
    p = 0
    n = len(s)
    for x in s:
        p+= x ** 2
    return p/n


"""
1 - Generate a sinusoidal discrete signal
2 - Generate a noisy signal
3 - Sum both
4 - Calculate power before and after

Power of a discrete signal
P \equal \over{1}{n} \sum^{n-1}_{n=0}|x[n]|^2
"""

# 1 - Generate a sinusoidal discrete signal
f_m = 0.01  # Sampling interval
f_s = 1     # Frequency of the sine wave
t_i = 0     # Initial time
t_f = 2     # Final time
amp = 5     # Amplitude of the sine wave
alpha = 0   # Phase shift

x, y = senoidal(f_m, f_s, t_i, t_f, amp, alpha)

# 2 - Generate a noisy signal
N = len(x)  # Number of samples
noise = np.random.normal(loc=0, scale=1, size=N)  # Mean=0, Std Dev=1

# 3 - Sum both
y_noisy = y + noise

print('Power before: ',power(y))
print('Power after: ',power(y_noisy))

# Plot the result
plt.plot(x, y, 'bo', markersize=3, label='Original Sine Wave')
plt.plot(x, y_noisy, 'ro', markersize=3, label='Noisy Sine Wave')
plt.title('Square Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()