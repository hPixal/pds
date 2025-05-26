import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import get_window

def sinusoidal(f_m, f_s, t_i, t_f, amp, alpha):
    x = np.arange(t_i, t_f, 1/f_m)
    y = amp * np.sin(2 * np.pi * f_s * x + alpha)
    return x, y

def main():
    f_s = 10
    t0 = 0
    tf = 1
    f_m = 200
    p_m = 1 / f_m

    # Generate a sinusoidal signal
    x, y = sinusoidal(f_m, f_s, t0, tf, 1, 0)
    N = len(x)

    hamming_window = get_window('hamming', N)
    barlett_window = get_window('bartlett', N)
    blackman_window = get_window('blackman', N)

    y_ham = y * hamming_window
    y_bar = y * barlett_window
    y_black = y * blackman_window

    Y = dft(y)
    Y_ham = dft(y_ham)
    Y_bar = dft(y_bar)
    Y_black = dft(y_black)

    freqs = np.fft.fftfreq(len(x), d=1 / f_m)  # frequency bins

    # Generate Dirac delta signal
    delta = dirac_delta(N, n0=N // 4)
    delta_ham = delta * hamming_window
    delta_bar = delta * barlett_window
    delta_black = delta * blackman_window

    Delta = dft(delta)
    Delta_ham = dft(delta_ham)
    Delta_bar = dft(delta_bar)
    Delta_black = dft(delta_black)

    # Plotting
    plt.figure(figsize=(18, 8))

    # Sinusoidal plots (left)
    plt.subplot(3, 2, 1)
    plt.plot(x, y, label='Original Signal')
    plt.title('Original Sinusoidal Signal')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)

    plt.subplot(3, 2, 3)
    plt.plot(x, y_ham, label='Hamming')
    plt.plot(x, y_bar, label='Bartlett')
    plt.plot(x, y_black, label='Blackman')
    plt.title('Windowed Sinusoidal Signal')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)

    plt.subplot(3, 2, 5)
    plt.stem(freqs[:N // 2], np.abs(Y)[:N // 2], basefmt=" ", linefmt='b-', markerfmt='bo', label='Original')
    plt.stem(freqs[:N // 2], np.abs(Y_ham)[:N // 2], basefmt=" ", linefmt='r-', markerfmt='ro', label='Hamming')
    plt.stem(freqs[:N // 2], np.abs(Y_bar)[:N // 2], basefmt=" ", linefmt='g-', markerfmt='go', label='Bartlett')
    plt.stem(freqs[:N // 2], np.abs(Y_black)[:N // 2], basefmt=" ", linefmt='m-', markerfmt='mo', label='Blackman')
    plt.legend()
    plt.title('DFT Magnitude (Sinusoidal)')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude')
    plt.grid(True)

    # Dirac delta plots (right)
    plt.subplot(3, 2, 2)
    plt.stem(x, delta, basefmt=" ", linefmt='b-', markerfmt='bo', label='Dirac Delta')
    plt.title('Dirac Delta Signal')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)

    plt.subplot(3, 2, 4)
    plt.plot(x, delta_ham, label='Hamming')
    plt.plot(x, delta_bar, label='Bartlett')
    plt.plot(x, delta_black, label='Blackman')
    plt.title('Windowed Dirac Delta')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)

    plt.subplot(3, 2, 6)
    plt.stem(freqs[:N // 2], np.abs(Delta)[:N // 2], basefmt=" ", linefmt='b-', markerfmt='bo', label='Original')
    plt.stem(freqs[:N // 2], np.abs(Delta_ham)[:N // 2], basefmt=" ", linefmt='r-', markerfmt='ro', label='Hamming')
    plt.stem(freqs[:N // 2], np.abs(Delta_bar)[:N // 2], basefmt=" ", linefmt='g-', markerfmt='go', label='Bartlett')
    plt.stem(freqs[:N // 2], np.abs(Delta_black)[:N // 2], basefmt=" ", linefmt='m-', markerfmt='mo', label='Blackman')
    plt.legend()
    plt.title('DFT Magnitude (Dirac Delta)')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude')
    plt.grid(True)

    plt.tight_layout()
    plt.show()
    

    
def dft(signal):
    N = len(signal)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += signal[n] * np.exp(-2j * np.pi * k * n / N)
    return X

def dirac_delta(N, n0=0):
    delta = np.zeros(N)
    if 0 <= n0 < N:
        delta[n0] = 1
    return delta

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