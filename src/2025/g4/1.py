import numpy as np
import matplotlib.pyplot as plt

def sinusoidal(f_m, f_s, t_i, t_f, amp, alpha):
    x = np.arange(t_i, t_f, f_m)
    y = amp * np.sin(2 * np.pi * f_s * x + alpha)
    return x, y

def main():
    f_s1 = 10;
    f_s2 = 20;
    f_s3 = 30;
    f_s4 = 40;

    t0 = 0;
    tf = 1;
    p_m = 0.001
    f_m = 1/p_m;
    
    # Generate a sinusoidal signal
    x, y1 = sinusoidal(p_m, f_s1, t0, tf, 1, 0)
    x, y2 = sinusoidal(p_m, f_s2, t0, tf, 1, 0)
    x, y3 = sinusoidal(p_m, f_s3, t0, tf, 1, 0)
    x, y4 = sinusoidal(p_m, f_s4, t0, tf, 1, 0)


    y = y1 + y2 + y3 + y4
    
    Y = dft(y)

    # Plot the original signal
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(x, y)
    plt.title('Sinusoidal Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    
    freqs = np.fft.fftfreq(len(x), d=1/f_m)  # frequency bins (can include negative freqs)

    # Plot the magnitude of the DFT
    plt.subplot(1, 2, 2)
    plt.stem(freqs, np.abs(Y))
    plt.title('DFT Magnitude')
    plt.xlabel('Frequency Bin')
    plt.ylabel('Magnitude')
    plt.tight_layout()
    plt.show()
    
    parseval(y)
    
def dft(signal):
    N = len(signal)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += signal[n] * np.exp(-2j * np.pi * k * n / N)
    return X

def energy(signal):
    N = len(signal)
    p2 = 0
    for n in range(N-1):
        p2 += abs(signal[n]) ** 2
    return p2

def parseval(x):
    N = len(x)
    X = dft(x)
    
    Xp2 = (1/N)*energy(X)
    xp2 = energy(x)
    
    print(f"xp2 (time domain): {xp2}")
    print(f"Xp2 (frequency domain): {Xp2}")
    
    if(xp2 == Xp2 ):
        print('Se cumple parseval')
        
main()