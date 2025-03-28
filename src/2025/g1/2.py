import numpy as np
import matplotlib.pyplot as plt

def sinusoidal(f_m, f_s, t_i, t_f, amp, alpha):
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

def invert_signal(y):
    return [-val for val in y]

def rectify_signal(y):
    return [abs(val) for val in y]

def exercise2():
    # Test the sinusoidal function
    f_m = 0.01  # Sampling interval
    f_s = 1     # Frequency of the sine wave
    t_i = 0     # Initial time
    t_f = 2     # Final time
    amp = 1     # Amplitude of the sine wave
    alpha = 0   # Phase shift

    x, y = sinusoidal(f_m, f_s, t_i, t_f, amp, alpha)
    y_q = quantizer(y, 0.25, 8)
    y_r = rectify_signal(y)
    y_i = invert_signal(y)
    
    # Plot the result
    plt.plot(x, y, label='Original Sine Wave')
    plt.plot(x, y_q, label='Quantized Sine Wave')
    plt.plot(x, y_r, label='Rectified Sine Wave')
    plt.plot(x, y_i, label='Inverted Sine Wave')
    
    plt.title('Sine Wave and Modifications')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)
    plt.show()
    
exercise2()