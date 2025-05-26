import numpy as np
import matplotlib.pyplot as plt

def sinusoidal(f_m, f_s, t_i, t_f, amp, alpha):
    x = np.arange(t_i, t_f, f_m)
    y = amp * np.sin(2 * np.pi * f_s * x + alpha)
    return x, y

def main():
    f_s = 10;
    t0 = 0;
    tf = 1;
    f_m = 100;
    p_m = 1/f_m;
    
    # Generate a sinusoidal signal
    x, y1 = sinusoidal(p_m, f_s, t0, tf, 1, 0)

    # Generate a shifted sinusoidal signal
    x, y2 = sinusoidal(p_m, f_s, t0, tf, 1, p_m*10)
    
    Y1 = dft(y1)
    Y2 = dft(y2)
    
    freqs = np.fft.fftfreq(len(x), d=1/f_m)  # frequency bins (can include negative freqs)

    # Plot the original signal
    plt.figure(figsize=(12, 5))
    plt.subplot(2, 2, 1)
    plt.stem(x, y1)
    plt.title('Sinusoidal Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    

    # Plot the magnitude of the DFT of Y1
    plt.subplot(2, 2, 2)
    plt.stem(freqs, np.abs(Y1))
    plt.title('DFT Magnitude')
    plt.xlabel('Frequency Bin')
    plt.ylabel('Magnitude')
    
    # Plot the shifted signal
    plt.subplot(2, 2, 3)
    plt.stem(x, y2)
    plt.title('Sinusoidal Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    
    # Plot the magnitude of the DFT of Y2
    plt.subplot(2, 2, 4)
    plt.stem(freqs, np.abs(Y2))
    plt.title('DFT Magnitude')
    plt.xlabel('Frequency Bin')
    plt.ylabel('Magnitude')
    plt.tight_layout()
    plt.show()
    
def dft(signal):
    N = len(signal)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += signal[n] * np.exp(-2j * np.pi * k * n / N)
    return X

main()