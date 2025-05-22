import numpy as np
import matplotlib.pyplot as plt

def senoidal(f_m, f_s, t_i, t_f, amp, alpha):
    dt = 1/f_m
    x = np.arange(t_i, t_f, dt)
    y = amp * np.sin(2 * np.pi * f_s * x + alpha)
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

def main():
    
    # Senoidal 2hz
    f_m = 100   # Sampling interval
    f_s = 2     # Frequency of the sine wave
    t_i = 0     # Initial time
    t_f = 1     # Final time
    amp = 1     # Amplitude of the sine wave
    alpha = 0   # Phase shift
    
    x_sen1,y_sen1 = senoidal(f_m, f_s, t_i, t_f, amp, alpha)
    x_sen2,y_sen2 = senoidal(f_m, f_s+2, t_i, t_f, amp, alpha)
    x_sqr,y_sqr   = square(f_m, f_s, t_i, t_f, amp, alpha)
    
    plt.plot(x_sen1, y_sen1, label='Senoidal 2Hz')
    plt.plot(x_sen2, y_sen2, label='Senoidal 4Hz')
    plt.plot(x_sqr, y_sqr, label='Square 2Hz')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Senoidal and Square Waves')
    plt.legend()
    plt.grid(True)
    plt.show()