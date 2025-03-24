import numpy as np
import matplotlib.pyplot as plt

def senoidal(f_m, f_s, t_i, t_f, amp, alpha):
    x = np.arange(t_i, t_f, f_m)
    y = amp * np.sin(2 * np.pi * f_s * x + alpha)
    return x, y

def sync(t_i, t_f, f_m):
    x = np.arange(t_i, t_f, f_m)
    y = []
    for t in x:
        if t != 0:
            y.append(np.sin(t) / t)
        else:
            y.append(1)
    return x, y

def square(f_m, f_s, t_i, t_f, amp, alpha):
    x = np.arange(t_i, t_f, f_m)
    y = []
    for t in x:
        mod = amp * np.sin(2 * np.pi * f_s * t + alpha)
        mod = mod*np.sign(mod)
        
        if mod < 0.5:
            y.append(1)
        else:
            y.append(-1)
    return x, y

def exercise1():
    # Test the senoidal function
    f_m = 0.01  # Sampling interval
    f_s = 1     # Frequency of the sine wave
    t_i = 0     # Initial time
    t_f = 2     # Final time
    amp = 1     # Amplitude of the sine wave
    alpha = 0   # Phase shift

    x, y = senoidal(f_m, f_s, t_i, t_f, amp, alpha)

    # Plot the result
    plt.plot(x, y)
    plt.title('Sine Wave')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

def exercise2():
    # Test the sync function
    t_i = -10     # Initial time
    t_f = 10    # Final time
    f_m = 0.01   # Sampling interval

    x, y = sync(t_i, t_f, f_m)

    # Plot the result
    plt.plot(x, y)
    plt.title('Sync Function')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

def exercise3():
    # Test the square function
    f_m = 0.01  # Sampling interval
    f_s = 0.5    # Frequency of the square wave
    t_i = -10     # Initial time
    t_f = 10     # Final time
    amp = 1     # Amplitude of the square wave
    alpha = 0   # Phase shift

    x, y = square(f_m, f_s, t_i, t_f, amp, alpha)

    # Plot the result
    plt.plot(x, y)
    plt.title('Square Wave')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()


exercise1()
exercise2()
exercise3()
