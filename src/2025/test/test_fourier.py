import scipy as sp
import numpy as np
import matplotlib.pyplot as plt


def sinusoidal(f_m, f_s, t_i, t_f, amp, alpha):
    x = np.arange(t_i, t_f, f_m)
    y = amp * np.sin(2 * np.pi * f_s * x + alpha)
    return x, y

def discrete_fourier_transform(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)

    for k in range(N):
        for n in range(N):
            X[k] += x[n]*np.e ** (-1j* 2*np.pi*k*n / N)
    
    return X

def main():
    # Test the senoidal function
    f_m = 0.01  # Sampling interval
    f_s = 1     # Frequency of the sine wave || This is what we should get by using the discrete fourier transform.
    t_i = 0     # Initial time
    t_f = 2     # Final time
    amp = 1     # Amplitude of the sine wave
    alpha = 0   # Phase shift

    # New sinusoidal wave with different frequency=1
    x, y = sinusoidal(f_m, f_s, t_i, t_f, amp, alpha)
    
    # New sinusoidal wave with different frequency=4
    x, y1 = sinusoidal(f_m, f_s+3, t_i, t_f, amp, alpha)
    
    # New sinusoidal wave with different frequency=11
    x, y2 = sinusoidal(f_m, f_s+10, t_i, t_f, amp, alpha)
    
    
    y = y + y1 + y2
    
    X = discrete_fourier_transform(y)
    
    N = len(y)
    freqs = np.fft.fftfreq(N, d=f_m)
    
      # Plot magnitude spectrum
    plt.figure(figsize=(10, 6))

    # Plot magnitude spectrum
    plt.subplot(2, 1, 1)
    plt.stem(freqs[:N//2], np.abs(X)[:N//2], basefmt=" ")
    plt.title("Discrete Fourier Transform (Magnitude)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid(True)

    # Plot sinusoidal function
    plt.subplot(2, 1, 2)
    plt.plot(x, y)
    plt.title("Sinusoidal Function")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)

    plt.tight_layout()
    plt.show()
    
main()